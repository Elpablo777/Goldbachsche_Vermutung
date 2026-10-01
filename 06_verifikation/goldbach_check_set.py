#!/usr/bin/env python3
"""
Zweite, unabhängige Prüfung der binären Goldbach-Aussage auf [4, N].

Methode A (goldbach_check.py): sortierte Primzahlliste, lineare Suche nach
kleinstem p, Lookup n-p im booleschen Sieb-Array.

Methode B (diese Datei): Menge (set) aller Primzahlen <= N; für jedes n
Existenzquantor p in primes mit p <= n/2 und (n-p) in der Menge.
Keine Abhängigkeit von der Reihenfolge der ersten Treffer außer für das
optionale minimale p (min über Generator).

Beide Methoden nutzen dasselbe Sieb nur als Primzahlgenerator; die
Goldbach-Suche ist strukturell verschieden (Array-Index vs. Hash-Set).
"""
from __future__ import annotations

import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "06_verifikation"


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    r = math.isqrt(limit)
    for i in range(2, r + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = 0
    return [i for i in range(2, limit + 1) if is_prime[i]]


def check_set(N: int) -> tuple[int, list[int], int | None, int, float]:
    t0 = time.perf_counter()
    primes = sieve_primes(N)
    prime_set = set(primes)
    failures: list[int] = []
    max_min_p = 2
    checked = 0
    for n in range(4, N + 1, 2):
        checked += 1
        half = n // 2
        witness = None
        for p in primes:
            if p > half:
                break
            if (n - p) in prime_set:
                witness = p
                break
        if witness is None:
            failures.append(n)
        elif witness > max_min_p:
            max_min_p = witness
    elapsed = time.perf_counter() - t0
    first = failures[0] if failures else None
    return checked, failures, first, max_min_p, elapsed


def main() -> int:
    N = 200_000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    checked, failures, first, max_min_p, elapsed = check_set(N)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"ergebnis_set_N{N}.txt"
    lines = [
        "BINÄRE GOLDBACH-VERIFIKATION METHODE B (set-membership)",
        f"Intervall: 4 <= n <= {N}, n gerade",
        "Methode: Primzahlmenge; Existenz p <= n/2 mit (n-p) in der Menge.",
        f"Geprüft: {checked}",
        f"Fehlschläge: {len(failures)}",
        f"Erster Fehlschlag: {first}",
        f"Max. minimales p: {max_min_p}",
        f"Laufzeit_s: {elapsed:.6f}",
        f"Python: {sys.version.split()[0]}",
        "",
        "BEWEISSTATUS: nur endlich; nicht G_bin für alle n.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
    print(f"geschrieben: {path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
