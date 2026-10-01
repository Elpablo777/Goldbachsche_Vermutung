#!/usr/bin/env python3
"""
Unabhaengiger Verifier fuer Witness-Dateien (GBWIT1-Format).

Prueft fuer eine Witness-Datei von Methode D (Go):
  1. Header, Laenge, CRC32 (IEEE) des Payloads.
  2. JEDES Witness (n, p): p prim, n-p prim, 2 <= p <= n/2  (Existenz).
  3. Minimialitaet: Neuberechnung des minimalen p per NumPy-Methode C
     (Vektoroperation ueber ungeloeste k=n/2) und Bytevergleich der
     resultierenden Witness-Werte mit der Datei.

Lauf:  python 06_verifikation/verify_witnesses.py 100000000 \
             06_verifikation/witnessen/witness_go_N100000000.bin
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


def read_witness_file(path: Path) -> tuple[int, np.ndarray]:
    data = path.read_bytes()
    if not data.startswith(b"GBWIT1\n"):
        raise ValueError("falscher Magic-Header")
    nl = data.index(b"\n", 7)
    N = int(data[7:nl].decode("ascii"))
    payload = data[nl + 1 : -4]
    crc_stored = int.from_bytes(data[-4:], "little")
    crc_calc = zlib.crc32(payload) & 0xFFFFFFFF
    if crc_stored != crc_calc:
        raise ValueError(f"CRC32 falsch: {crc_stored:#010x} != {crc_calc:#010x}")
    kmax = N // 2
    w = np.zeros(kmax + 1, dtype=np.int64)
    # LEB128 dekodieren; alle Werte < 2^14, mehrheitlich 1 Byte.
    pos = 0
    n_bytes = len(payload)
    vals = np.empty(kmax - 1, dtype=np.int64)
    i = 0
    payload_mv = memoryview(payload)
    # Schneller Pfad: Laufe bis ein Byte >= 0x80 kommt ( Mehrbyte-Varint ).
    while i < kmax - 1:
        b0 = payload[pos]
        if b0 < 0x80:
            vals[i] = b0
            pos += 1
            i += 1
            continue
        # Mehrbyte-Varint (selten)
        shift = 0
        v = 0
        while True:
            b = payload[pos]
            pos += 1
            v |= (b & 0x7F) << shift
            shift += 7
            if b < 0x80:
                break
        vals[i] = v
        i += 1
    if pos != n_bytes:
        raise ValueError(f"Payload-Laenge {n_bytes} != dekodierte Position {pos}")
    w[2:] = vals
    return N, w


def sieve_bool(limit: int) -> np.ndarray:
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    r = math.isqrt(limit)
    for i in range(2, r + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def main() -> int:
    N = int(sys.argv[1])
    path = Path(sys.argv[2])
    if N < 4 or N % 2 != 0:
        print("N muss gerade und >= 4 sein", file=sys.stderr)
        return 2

    t0 = time.perf_counter()
    N_file, w = read_witness_file(path)
    kmax = N // 2
    checks: list[str] = []
    ok = True

    sha = hashlib.sha256(path.read_bytes()).hexdigest()

    # Check 0: Header
    header_ok = N_file == N
    checks.append(("Header-N stimmt: " + str(header_ok), header_ok))
    ok &= header_ok

    # Check 1: alle Witness > 0 vorhanden
    missing = int((w[2:] == 0).sum())
    checks.append((f"Anzahl fehlender Witness (soll 0): {missing}", missing == 0))
    ok &= missing == 0

    s = sieve_bool(N)
    k = np.arange(2, kmax + 1, dtype=np.int64)
    wp = w[k]  # int64

    # Check 2: p <= n/2 = k
    bound_ok = bool((wp <= k).all())
    checks.append((f"Alle p <= n/2: {bound_ok}", bound_ok))
    ok &= bound_ok

    # Check 3: p prim
    p_prime = bool(s[wp].all())
    checks.append((f"Alle p prim: {p_prime}", p_prime))
    ok &= p_prime

    # Check 4: n-p prim
    q = (2 * k - wp).astype(np.int64)
    q_prime = bool(s[q].all())
    checks.append((f"Alle n-p prim: {q_prime}", q_prime))
    ok &= q_prime

    t_exist = time.perf_counter()

    # Check 5: Minimalitaet via Methode-C-Neuberechnung
    primes_arr = np.flatnonzero(s).astype(np.int64)
    primes = primes_arr.tolist()
    w2 = np.zeros(kmax + 1, dtype=np.int64)
    remaining = k.copy()
    max_p = 2
    for p in primes:
        if not remaining.size or p > kmax:
            break
        ge = remaining >= p
        remaining = remaining[ge]
        if not remaining.size:
            break
        qq = 2 * remaining - p
        hit = s[qq]
        ks = remaining[hit]
        if ks.size:
            w2[ks] = p
            if p > max_p:
                max_p = p
            remaining = remaining[~hit]
    minimal_ok = bool((w2[2:] == w[2:]).all())
    checks.append(
        (
            f"Minimalitaet (Neuberechnung identisch): {minimal_ok}, max min p={max_p}",
            minimal_ok,
        )
    )
    ok &= minimal_ok

    elapsed = time.perf_counter() - t0
    lines = [
        "WITNESS-VERIFIKATION (unabhaengig, Python/NumPy)",
        f"Datei: {path}",
        f"Groesse_Bytes: {path.stat().st_size}",
        f"SHA256: {sha}",
        f"Intervall: 4 <= n <= {N}",
        f"Gepruefte gerade n: {kmax - 1}",
        "",
        "Checks:",
    ]
    for text, good in checks:
        lines.append(("  [OK]   " if good else "  [FEHL] ") + text)
    lines += [
        "",
        f"Existenz-Checks Laufzeit_s: {t_exist - t0:.3f}",
        f"Gesamtlaufzeit_s: {elapsed:.3f}",
        f"Python: {sys.version.split()[0]}, NumPy: {np.__version__}",
        "",
        "Bei allen [OK]: jede gerade Zahl in [4,N] besitzt eine Goldbach-Partition;",
        " Witness-Gueltigkeit UND Minimalitaet sind durch zwei unabhaengige",
        " Implementierungen (Go + NumPy) bestaetigt. Kein Beweis fuer n > N.",
    ]
    report = OUT_VER / f"verify_report_N{N}.txt"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(report.read_text(encoding="utf-8"))
    print("geschrieben:", report)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
