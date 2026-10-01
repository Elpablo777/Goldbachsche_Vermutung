#!/usr/bin/env python3
"""
Verifier v2: vollstaendige, speicheroptimierte Gegenpruefung von GBWIT1-
Witness-Dateien auch fuer N = 10^9 (int32-Arithmetik, gechunkter
vektorisierter LEB128-Decoder, gestreamte Validitaetspruefung).

Prueft:
  1. Header, CRC32 (IEEE) ueber den Payload, Tokenanzahl.
  2. JEDES Witness p(n): 2 <= p <= n/2, p prim, n-p prim  (Existenz).
  3. Minimialitaet: komplette Neuberechnung des minimalen p (Methode C,
     NumPy, int32) und Byte-fuer-Byte-Vergleich mit der Datei.

Vor Einsatz auf 10^9 wurde dieser Verifier gegen die bereits vollstaendig
gepruefte 10^8-Datei validiert (identische Resultate wie verify_witnesses.py).

Aufruf:
  python 06_verifikation/verify_witnesses2.py 1000000000 <witness.bin>
Exitcode 0 nur wenn alle Checks bestehen.
"""
from __future__ import annotations

import hashlib
import math
import sys
import time
import zlib
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT_VER = ROOT / "06_verifikation"
CHUNK_BYTES = 1 << 26  # 64 MiB Payload pro Decode-Chunk


def sieve_bool(limit: int) -> np.ndarray:
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    r = math.isqrt(limit)
    for i in range(2, r + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def compute_minimal_witnesses(s: np.ndarray, kmax: int) -> tuple[np.ndarray, int]:
    """Methode C (int32): minimales p fuer n=2k, k=2..kmax."""
    primes = np.flatnonzero(s).astype(np.int64).tolist()
    w2 = np.zeros(kmax + 1, dtype=np.int32)
    remaining = np.arange(2, kmax + 1, dtype=np.int32)
    max_p = 2
    for p in primes:
        if not remaining.size or p > kmax:
            break
        remaining = remaining[remaining >= p]
        if not remaining.size:
            break
        q = 2 * remaining - p  # <= 2*kmax <= N+1, int32-sicher fuer N < 2^30
        hit = s[q]
        ks = remaining[hit]
        if ks.size:
            w2[ks] = p
            if p > max_p:
                max_p = p
            remaining = remaining[~hit]
    return w2, max_p


def iter_token_chunks(payload: bytes):
    """Yieldet (token_start_indices_lokal, werte, globaler_token_offset).

    Vektorisierter LEB128-Decoder (Tokenwerte < 16384, max. 2 Bytes/Token);
    Chunks beginnen garantiert an einer Token-Grenze. Erzeugt keine
    grossen Zwischenarrays (Chunk-Weise).
    """
    n = len(payload)
    barr = np.frombuffer(payload, dtype=np.uint8)
    pos = 0
    token_offset = 0
    is2_global_shift = 0  # Anzahl 2-Byte-Tokens vor dem Chunk
    while pos < n:
        # Chunk-Start an Token-Grenze ausrichten
        if pos > 0 and barr[pos - 1] >= 128:
            pos += 1  # Follower-Byte des vorherigen Tokens
        if pos >= n:
            break
        end = min(pos + CHUNK_BYTES, n)
        seg = barr[pos:end]
        # Falls das letzte Segment-Byte ein 2-Byte-Start ist, gehört das
        # nächste Byte dazu: include one extra byte as follower data.
        include_extra = end < n and seg[-1] >= 128
        if include_extra:
            seg = barr[pos : end + 1]
        is2 = seg >= 128
        if include_extra:
            is2[-1] = False  # Extra-Byte ist nur Follower-Daten
        # Follower: Position unmittelbar nach einem 2-Byte-Start
        follower = np.zeros(len(seg), dtype=bool)
        follower[1:] = is2[:-1]
        starts = ~follower
        # Sicherheitsnetz: keine 3-Byte-Tokens (Follower muss < 128 sein)
        if is2[follower].any():
            raise ValueError("3-Byte-Varint angetroffen (Token >= 16384) — Formatfrage, Abbruch")
        s_idx = np.flatnonzero(starts)
        is2_s = is2[s_idx]
        # out index = s - (#2-Byte-Starts vor s)
        cum = np.cumsum(is2, dtype=np.int64)
        out = s_idx.astype(np.int64) - (cum[s_idx] - is2_s.astype(np.int64)) + token_offset
        vals = seg[s_idx].astype(np.int64)
        two = is2_s
        if two.any():
            vals[two] = (seg[s_idx[two]].astype(np.int64) & 0x7F) + (
                seg[s_idx[two] + 1].astype(np.int64) << 7
            )
        n_tokens = int(starts.sum())
        yield out, vals, n_tokens
        token_offset += n_tokens
        is2_global_shift += int(is2_s.sum())
        pos = end


def main() -> int:
    N = int(sys.argv[1])
    path = Path(sys.argv[2])
    if N < 4 or N % 2 != 0:
        print("N muss gerade und >= 4 sein", file=sys.stderr)
        return 2
    kmax = N // 2

    t0 = time.perf_counter()
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    if not data.startswith(b"GBWIT1\n"):
        print("FEHLER: falscher Magic-Header", file=sys.stderr)
        return 1
    nl = data.index(b"\n", 7)
    N_file = int(data[7:nl].decode("ascii"))
    payload = data[nl + 1 : -4]
    crc_stored = int.from_bytes(data[-4:], "little")
    crc_calc = zlib.crc32(payload) & 0xFFFFFFFF
    del data

    checks: list[tuple[str, bool]] = []
    ok = True

    header_ok = N_file == N
    checks.append((f"Header-N stimmt ({N_file}): {header_ok}", header_ok))
    crc_ok = crc_stored == crc_calc
    checks.append((f"CRC32 stimmt ({crc_calc:#010x}): {crc_ok}", crc_ok))
    ok &= header_ok and crc_ok

    t_sieve = time.perf_counter()
    s = sieve_bool(N)
    t_sieve = time.perf_counter() - t_sieve

    # ---- Durchlauf 1: Methode-C-Neuberechnung (Minimalitaet) ----
    t_c = time.perf_counter()
    w2, max_p_recomputed = compute_minimal_witnesses(s, kmax)
    t_c = time.perf_counter() - t_c

    # ---- Durchlauf 2: gestreamtes Dekodieren + Validitaet + Vergleich ----
    t_stream = time.perf_counter()
    n_tokens_seen = 0
    fail_p_prime = fail_q_prime = fail_bound = fail_mismatch = 0
    first_bad: int | None = None
    for out, vals, n_tokens in iter_token_chunks(payload):
        k = out.astype(np.int64) + 2  # Token i <-> k = i+2
        n_tokens_seen += n_tokens
        p = vals
        if (p < 2).any() or (p > k).any():
            fail_bound += int(((p < 2) | (p > k)).sum())
        pp = s[p]
        if not pp.all():
            fail_p_prime += int((~pp).sum())
        q = 2 * k - p
        qq = s[q]
        if not qq.all():
            fail_q_prime += int((~qq).sum())
        # Minimalitaetsvergleich mit Methode C
        same = w2[k] == p
        if not same.all():
            fail_mismatch += int((~same).sum())
            if first_bad is None:
                first_bad = int(2 * k[~same][0])
        bad = (~pp) | (~qq) | (p < 2) | (p > k) | (~same)
        if bad.any() and first_bad is None:
            first_bad = int(2 * k[bad][0])
    t_stream = time.perf_counter() - t_stream

    expected = kmax - 1
    count_ok = n_tokens_seen == expected
    checks.append((f"Tokenanzahl = {n_tokens_seen} (erwartet {expected}): {count_ok}", count_ok))
    checks.append((f"Alle 2 <= p <= n/2 (Verletzungen: {fail_bound}): {fail_bound == 0}", fail_bound == 0))
    checks.append((f"Alle p prim (Verletzungen: {fail_p_prime}): {fail_p_prime == 0}", fail_p_prime == 0))
    checks.append((f"Alle n-p prim (Verletzungen: {fail_q_prime}): {fail_q_prime == 0}", fail_q_prime == 0))
    checks.append(
        (
            f"Minimalitaet = Methode C, max min-p = {max_p_recomputed} (Abweichungen: {fail_mismatch}): {fail_mismatch == 0}",
            fail_mismatch == 0,
        )
    )
    ok &= count_ok and fail_bound == 0 and fail_p_prime == 0 and fail_q_prime == 0 and fail_mismatch == 0

    elapsed = time.perf_counter() - t0
    lines = [
        "WITNESS-VERIFIKATION v2 (unabhaengig, Python/NumPy, int32 + gechunkter Decoder)",
        f"Datei: {path}",
        f"Groesse_Bytes: {path.stat().st_size}",
        f"SHA256: {sha}",
        f"Intervall: 4 <= n <= {N}",
        f"Gepruefte gerade n: {expected}",
        "",
        "Checks:",
    ]
    for text, good in checks:
        lines.append(("  [OK]   " if good else "  [FEHL] ") + text)
    lines += [
        "",
        f"Sieb-Aufbau_s: {t_sieve:.3f}",
        f"Miniminalitaet-Neuberechnung_s: {t_c:.3f}",
        f"Stream-Decode+Validitaet_s: {t_stream:.3f}",
        f"Gesamtlaufzeit_s: {elapsed:.3f}",
        f"Python: {sys.version.split()[0]}, NumPy: {np.__version__}",
        "",
        "Bei allen [OK]: jede gerade Zahl in [4,N] besitzt eine Goldbach-Partition;",
        " Gueltigkeit UND Minimalitaet jedes einzelnen Witness durch unabhaengige",
        " Neuberechnung bestaetigt. Kein Beweis fuer n > N.",
    ]
    report = OUT_VER / f"verify2_report_N{N}.txt"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(report.read_text(encoding="utf-8"))
    print("geschrieben:", report)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
