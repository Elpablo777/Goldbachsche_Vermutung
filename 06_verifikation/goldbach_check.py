#!/usr/bin/env python3
"""
Reproduzierbare Prüfung der binären Goldbach-Aussage
für alle geraden n mit 4 <= n <= N.

Dies ist KEIN Beweis der Vermutung für alle n, sondern eine
endliche, nachvollziehbare Verifikation auf einem expliziten Intervall.

Ausgabe:
  06_verifikation/ergebnis_NXXXXX.txt
  04_rechnungen/partitionen_klein.txt
  04_rechnungen/singular_series_stichprobe.txt
"""
from __future__ import annotations

import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_VER = ROOT / "06_verifikation"
OUT_REC = ROOT / "04_rechnungen"


def sieve_eratosthenes(limit: int) -> tuple[list[int], bytearray]:
    if limit < 2:
        return [], bytearray(limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    r = int(math.isqrt(limit))
    for i in range(2, r + 1):
        if is_prime[i]:
            start = i * i
            for j in range(start, limit + 1, i):
                is_prime[j] = 0
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes, is_prime


def goldbach_witness(n: int, primes: list[int], is_prime: bytearray) -> tuple[int, int] | None:
    """Minimale Partition: kleinstes p mit p + q = n, q prim, p <= q."""
    half = n // 2
    for p in primes:
        if p > half:
            break
        q = n - p
        if q <= limit_of(is_prime) and is_prime[q]:
            return p, q
    return None


def limit_of(is_prime: bytearray) -> int:
    return len(is_prime) - 1


def twin_odd_prime_product_constant() -> float:
    """prod_{p>2} (1 - 1/(p-1)^2), numerisch bis großer Primzahlschranke."""
    # Wird in main mit dem Sieb berechnet.
    return 0.0


def hardy_littlewood_S(n: int, primes: list[int]) -> float:
    """
    Singuläre Reihe (Hardy–Littlewood) für gerade n:
      S(n) = 2 * prod_{p>2} (1 - 1/(p-1)^2) * prod_{p|n, p>2} (p-1)/(p-2)
    Das unendliche Produkt wird durch Primzahlen bis max(n, 10^5) approximiert.
    """
    if n % 2 != 0:
        raise ValueError("S(n) hier nur für gerade n")
    cap = max(n, 100_000)
    prod_inf = 1.0
    extra = 1.0
    for p in primes:
        if p > cap:
            break
        if p == 2:
            continue
        prod_inf *= 1.0 - 1.0 / ((p - 1) ** 2)
        if n % p == 0:
            extra *= (p - 1) / (p - 2)
    return 2.0 * prod_inf * extra


def count_representations(n: int, primes: list[int], is_prime: bytearray) -> int:
    """Anzahl ungeordneter Partitionen p+q=n mit p<=q prim."""
    c = 0
    half = n // 2
    for p in primes:
        if p > half:
            break
        if is_prime[n - p]:
            c += 1
    return c


def main() -> int:
    N = 200_000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    if N < 4 or N % 2 != 0:
        print("N muss gerade und >= 4 sein", file=sys.stderr)
        return 2

    t0 = time.perf_counter()
    primes, is_prime = sieve_eratosthenes(N)
    failures: list[int] = []
    first_fail = None
    checked = 0
    max_small_prime_needed = 2
    examples: list[tuple[int, int, int]] = []

    for n in range(4, N + 1, 2):
        w = goldbach_witness(n, primes, is_prime)
        checked += 1
        if w is None:
            failures.append(n)
            if first_fail is None:
                first_fail = n
            continue
        p, q = w
        if p > max_small_prime_needed:
            max_small_prime_needed = p
        if n <= 100:
            examples.append((n, p, q))

    elapsed = time.perf_counter() - t0

    OUT_VER.mkdir(parents=True, exist_ok=True)
    OUT_REC.mkdir(parents=True, exist_ok=True)

    report = OUT_VER / f"ergebnis_N{N}.txt"
    lines = [
        "BINÄRE GOLDBACH-VERIFIKATION (endlich)",
        f"Intervall: alle geraden n mit 4 <= n <= {N}",
        f"Methode: lineares Sieb des Eratosthenes bis {N}, dann für jedes n",
        "         kleinstes p <= n/2 mit n-p prim (exakte Integer-Arithmetik).",
        f"Anzahl geprüfter gerader n: {checked}",
        f"Anzahl Fehlschläge: {len(failures)}",
        f"Erster Fehlschlag: {first_fail}",
        f"Größtes benötigtes kleinstes Summandenprimzahl p(n) im Intervall: {max_small_prime_needed}",
        f"Anzahl Primzahlen <= {N}: {len(primes)}",
        f"Laufzeit_s: {elapsed:.6f}",
        f"Python: {sys.version.split()[0]}",
        "",
        "BEWEISSTATUS DIESES LAUFS:",
        "  Wenn Fehlschläge=0, gilt: die Aussage ist wahr für alle geraden n in [4,N].",
        "  Daraus folgt NICHT die Aussage für alle geraden n >= 4.",
        "",
    ]
    if failures:
        lines.append("FEHLERLISTE (erste 50): " + ", ".join(map(str, failures[:50])))
    else:
        lines.append("KEINE Gegenbeispiele im Intervall.")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    part_path = OUT_REC / "partitionen_klein.txt"
    part_lines = [
        "Minimale Goldbach-Partitionen p + q = n für 4 <= n <= 100, p <= q.",
        "Berechnet durch goldbach_check.py (exakt).",
        "",
        f"{'n':>6} {'p':>6} {'q':>6}",
    ]
    for n, p, q in examples:
        part_lines.append(f" {n:5d} {p:6d} {q:6d}")
    part_path.write_text("\n".join(part_lines) + "\n", encoding="utf-8")

    # Stichprobe singuläre Reihe vs. Zählung
    sample_n = [10, 12, 30, 100, 210, 1000, 10080, 30030]
    sample_n = [n for n in sample_n if n <= N]
    ss_path = OUT_REC / "singular_series_stichprobe.txt"
    ss = [
        "Hardy–Littlewood-Vergleich (heuristisch, KEIN Beweis):",
        "  G_2(n) := Anzahl ungeordneter Partitionen p+q=n, p<=q prim",
        "  Asymptotik (Vermutung): G_2(n) ~ S(n) * n / (log n)^2",
        "  (Normierung hier: S(n) wie oben mit Vorfaktor 2 im unendlichen Produkt.)",
        "",
        f"{'n':>8} {'G2':>8} {'S(n)':>14} {'S*n/(log n)^2':>16} {'Verhaeltnis':>12}",
    ]
    for n in sample_n:
        g2 = count_representations(n, primes, is_prime)
        S = hardy_littlewood_S(n, primes)
        pred = S * n / (math.log(n) ** 2)
        ratio = g2 / pred if pred else float("nan")
        ss.append(f"{n:8d} {g2:8d} {S:14.8f} {pred:16.4f} {ratio:12.6f}")
    ss.append("")
    ss.append("Interpretation: Verhältnis nahe 1 stützt die Heuristik, beweist sie nicht.")
    ss_path.write_text("\n".join(ss) + "\n", encoding="utf-8")

    print(report.read_text(encoding="utf-8"))
    print(f"geschrieben: {report}")
    print(f"geschrieben: {part_path}")
    print(f"geschrieben: {ss_path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
