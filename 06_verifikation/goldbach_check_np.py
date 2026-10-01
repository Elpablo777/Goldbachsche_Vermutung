#!/usr/bin/env python3
"""
Methode C: vektorisierte Goldbach-Verifikation mit NumPy.

Strukturell unabhaengig von Methode A (goldbach_check.py: Liste + lineare
Suche) und Methode B (goldbach_check_set.py: Hash-Set):
  - Primzahlsieb als NumPy-Boolean-Array mit Slice-Zuweisung,
  - Witness-Suche als Vektoroperation ueber die noch ungeloessten geraden n,
  - minimales p durch aufsteigende Iteration ueber die Primzahlen.

Korrektheitsargument fuer "dead"-Kandidaten (n ohne Witness):
  Ein k = n/2 ist genau dann endgueltig tot, wenn jede Primzahl p <= k
  bereits getestet wurde und 2k-p zusammengesetzt war. Der Pass mit
  p = k+1 verschiebt alle k < p in die Failure-Liste; zuvor wurde k in
  jedem Pass p' <= k getestet (q = 2k-p' >= k >= 2 stets definiert).

Dies ist KEIN Beweis von G_bin fuer alle n, sondern eine endliche,
reproduzierbare Verifikation auf [4, N].

Optionales Witness-Datei-Format (identisch zu Methode D/Go, siehe
ANLEITUNG.md):
  Zeile 1: "GBWIT1"
  Zeile 2: N (dezimal)
  Payload: LEB128-Varints des minimalen p fuer n = 4, 6, ..., N (in dieser
           Reihenfolge)
  Trailer: 4 Bytes CRC32 (IEEE, little-endian) ueber den Payload.
"""
from __future__ import annotations

import math
import sys
import time
import zlib
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT_VER = ROOT / "06_verifikation"
OUT_REC = ROOT / "04_rechnungen"


def sieve_bool(limit: int) -> np.ndarray:
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    r = math.isqrt(limit)
    for i in range(2, r + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def write_witness_file(path: Path, N: int, w: np.ndarray) -> None:
    """w[k] = minimales p fuer n = 2k (k = 2..N//2); 0 = kein Witness."""
    payload = bytearray()
    for k in range(2, N // 2 + 1):
        p = int(w[k])
        if p <= 0:
            raise RuntimeError(f"kein Witness fuer n={2*k}; Witness-Datei unvollstaendig")
        while True:
            b = p & 0x7F
            p >>= 7
            if p:
                payload.append(b | 0x80)
            else:
                payload.append(b)
                break
    crc = zlib.crc32(bytes(payload)) & 0xFFFFFFFF
    with open(path, "wb") as f:
        f.write(b"GBWIT1\n")
        f.write(f"{N}\n".encode("ascii"))
        f.write(bytes(payload))
        f.write(crc.to_bytes(4, "little"))


def singular_series(n: int, primes: list[int]) -> float:
    """S(n) = 2 * prod_{p>2}(1-1/(p-1)^2) * prod_{p|n, p>2} (p-1)/(p-2),
    Produkt abgeschnitten bei 10^5 (Relativfehler < 1e-5)."""
    prod_inf = 1.0
    extra = 1.0
    for p in primes:
        if p > 100_000:
            break
        if p == 2:
            continue
        prod_inf *= 1.0 - 1.0 / ((p - 1) * (p - 1))
        if n % p == 0:
            extra *= (p - 1) / (p - 2)
    return 2.0 * prod_inf * extra


def main() -> int:
    N = 200_000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    witness_path: Path | None = None
    if len(sys.argv) > 2:
        witness_path = Path(sys.argv[2])
    if N < 4 or N % 2 != 0:
        print("N muss gerade und >= 4 sein", file=sys.stderr)
        return 2

    t0 = time.perf_counter()
    s = sieve_bool(N)
    primes_arr = np.flatnonzero(s).astype(np.int64)
    primes = primes_arr.tolist()
    kmax = N // 2

    # Witness je k = n/2: 0 = ungelöst. int32 reicht (p <= ~1e5 << 2^31).
    w = np.zeros(kmax + 1, dtype=np.int32)

    remaining = np.arange(2, kmax + 1, dtype=np.int64)
    failures: list[int] = []
    max_p = 2
    records: list[tuple[int, int, int]] = []  # (p, erstes n, Anzahl n)
    passes = 0

    for p in primes:
        if not remaining.size:
            break
        if p > kmax:
            break
        passes += 1
        ge = remaining >= p
        dead = remaining[~ge]
        if dead.size:
            failures.extend((2 * dead).tolist())
            remaining = remaining[ge]
        if not remaining.size:
            break
        q = 2 * remaining - p
        hit = s[q]
        ks = remaining[hit]
        if ks.size:
            w[ks] = p
            if p > max_p:
                records.append((p, int(2 * ks.min()), int(ks.size)))
                max_p = p
            remaining = remaining[~hit]

    if remaining.size:
        failures.extend((2 * remaining).tolist())
        remaining = remaining[:0]

    elapsed = time.perf_counter() - t0
    checked = kmax - 1  # k = 2..kmax -> n = 4..N

    if witness_path is not None:
        write_witness_file(witness_path, N, w)

    OUT_VER.mkdir(parents=True, exist_ok=True)
    report = OUT_VER / f"ergebnis_np_N{N}.txt"

    # Blockweise Maxima der minimalen Summandenprimzahl
    blocks: list[tuple[int, int, int]] = []  # [A, B] -> max min-p, erstes n
    a = 4
    mag = 1
    while a <= N:
        b = min(10 ** mag, N)
        ka, kb = (a + 1) // 2, b // 2
        seg = w[ka : kb + 1]
        m = int(seg.max()) if seg.size else 0
        first = int(2 * (ka + int(np.argmax(seg)))) if (seg.size and m > 0) else 0
        blocks.append((a, b, m, first))
        a = b + 1
        mag += 1

    lines = [
        "BINÄRE GOLDBACH-VERIFIKATION METHODE C (NumPy, vektorisiert)",
        f"Intervall: alle geraden n mit 4 <= n <= {N}",
        "Methode: NumPy-Sieb (Slice-Zuweisung); Witness-Zuweisung als",
        "         Vektoroperation ueber ungeloeste k=n/2, p aufsteigend;",
        "         'dead'-k (k<p) sind endgueltige Fehlschlaege (siehe Header).",
        f"Anzahl geprüfter gerader n: {checked}",
        f"Anzahl Fehlschläge: {len(failures)}",
        f"Erster Fehlschlag: {min(failures) if failures else None}",
        f"Größtes minimales p(n): {max_p}",
        f"Anzahl Primzahlen <= {N}: {len(primes)}",
        f"Anzahl Witness-Pässe: {passes}",
        f"Laufzeit_s: {elapsed:.6f}",
        f"Python: {sys.version.split()[0]}",
        f"NumPy: {np.__version__}",
        f"Plattform: {sys.platform}",
        "",
        "Rekordhalter (p, erstes n mit min-p = p, Anzahl n mit diesem Rekord):",
    ]
    for p, n_first, cnt in records:
        lines.append(f"  p={p:6d}  n_erste={n_first:12d}  anzahl={cnt}")
    lines.append("")
    lines.append("Maximales minimales p(n) pro Zehnerpotz-Block [A,B]:")
    for a, b, m, first in blocks:
        lines.append(f"  [{a:>12d}, {b:>12d}]  max_min_p={m:6d}  erstes_n={first:12d}")
    lines += [
        "",
        "BEWEISSTATUS DIESES LAUFS:",
        "  Wenn Fehlschlaege=0: die Aussage gilt fuer alle geraden n in [4,N].",
        "  Daraus folgt NICHT die Aussage fuer alle geraden n >= 4.",
        "",
    ]
    if failures:
        lines.append("FEHLERLISTE (erste 50): " + ", ".join(map(str, failures[:50])))
    else:
        lines.append("KEINE Gegenbeispiele im Intervall.")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Goldbach-Komet: korrigierte Normierung G_2(n) ~ (1/2) S(n) n/(log n)^2
    sample = [n for n in (1000, 10000, 100000, 1000000, 10000000, 30030, 510510, 2**23) if n <= N]
    ss_path = OUT_REC / "goldbach_komet_normiert.txt"
    ss = [
        "Goldbach-Komet mit KORRIGIERTER Normierung (Heuristik, KEIN Beweis):",
        "  G_2(n) = Anzahl ungeordneter Partitionen p+q=n (p<=q, prim)",
        "  Erwartung (Hardy-Littlewood, geordnete Zaehlung S(n)*n/log^2 n):",
        "    G_2(n) ~ (1/2) * S(n) * n / (log n)^2   (Faktor 1/2: Unordnung)",
        "  S(n) = 2*prod_{p>2}(1-1/(p-1)^2)*prod_{p|n,p>2}(p-1)/(p-2),",
        "  unendliches Produkt abgeschnitten bei p<=10^5.",
        "",
        f"{'n':>12} {'G2(n)':>10} {'1/2*S*n/log^2n':>16} {'Verhaeltnis':>12}",
    ]
    for n in sample:
        ps = primes_arr[primes_arr <= n // 2]
        g2 = int(s[n - ps].sum())
        S = singular_series(n, primes)
        pred = 0.5 * S * n / (math.log(n) ** 2)
        ratio = g2 / pred if pred > 0 else float("nan")
        ss.append(f"{n:12d} {g2:10d} {pred:16.2f} {ratio:12.6f}")
    ss.append("")
    ss.append("Interpretation: Verhaeltnis nahe 1 staerkt die Heuristik, beweist sie nicht.")
    ss_path.write_text("\n".join(ss) + "\n", encoding="utf-8")

    print(report.read_text(encoding="utf-8"))
    print(f"geschrieben: {report}")
    if witness_path is not None:
        print(f"geschrieben: {witness_path}")
    print(f"geschrieben: {ss_path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
