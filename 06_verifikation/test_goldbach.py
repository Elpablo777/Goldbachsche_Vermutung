#!/usr/bin/env python3
"""Gegenprüfung: Methode A vs. B auf kleinem N; Satz-4-Partitionen."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06_verifikation"))

from goldbach_check import goldbach_witness, sieve_eratosthenes  # noqa: E402
from goldbach_check_set import check_set, sieve_primes  # noqa: E402

SATZ4 = {
    4: (2, 2),
    6: (3, 3),
    8: (3, 5),
    10: (3, 7),
    12: (5, 7),
    14: (3, 11),
    16: (3, 13),
    18: (5, 13),
    20: (3, 17),
    22: (3, 19),
    24: (5, 19),
    26: (3, 23),
    28: (5, 23),
    30: (7, 23),
}


def test_satz4_witnesses() -> None:
    primes, is_prime = sieve_eratosthenes(30)
    for n, (p, q) in SATZ4.items():
        w = goldbach_witness(n, primes, is_prime)
        assert w == (p, q), (n, w, (p, q))
        assert p + q == n


def test_methods_agree_N1000() -> None:
    N = 1000
    primes, is_prime = sieve_eratosthenes(N)
    fails_a = []
    for n in range(4, N + 1, 2):
        if goldbach_witness(n, primes, is_prime) is None:
            fails_a.append(n)
    checked, fails_b, _, max_p_b, _ = check_set(N)
    assert checked == N // 2 - 1  # 4,6,...,1000 → 499
    assert fails_a == []
    assert fails_b == []
    # minimales p Methode A
    max_p_a = 2
    for n in range(4, N + 1, 2):
        p, _q = goldbach_witness(n, primes, is_prime)
        if p > max_p_a:
            max_p_a = p
    assert max_p_a == max_p_b


def test_sieve_counts() -> None:
    assert len(sieve_primes(10)) == 4  # 2,3,5,7
    assert len(sieve_primes(200000)) == 17984


# --- Sätze 5-6 (ELEMENTARE_SAETZE.md, 2026-10-01) ---

KETTE = [3, 5, 7, 13, 23, 43, 83, 163, 317, 631, 1259, 2503, 5003, 8009, 10007]


def test_kette_primzahlen_und_luecken() -> None:
    """Satz 5, Schritt 2: Kettenprimzahlen prim, jede < 2x Vorgänger."""
    limit = KETTE[-1]
    primes, is_prime = sieve_eratosthenes(limit)
    for p in KETTE:
        assert is_prime[p], p
    for a, b in zip(KETTE, KETTE[1:]):
        assert b < 2 * a, (a, b)


def test_bertrand_bis_100000() -> None:
    """Satz 5 numerisch: für jedes n in [1, 100000] existiert p in (n, 2n]."""
    LIMIT = 100000
    _, is_prime = sieve_eratosthenes(2 * LIMIT)
    for n in range(1, LIMIT + 1):
        assert any(is_prime[p] for p in range(n + 1, 2 * n + 1)), n


def test_satz6_zerlegung_bis_5000() -> None:
    """Satz 6 konstruktiv: n zerfällt in <= floor(log2 n)+1 Primzahlen."""
    import math

    LIMIT = 5000
    primes, is_prime = sieve_eratosthenes(LIMIT)
    prime_list = [p for p in primes]

    def zerlege(n: int) -> list[int]:
        parts: list[int] = []
        while n > 0:
            if is_prime[n]:
                parts.append(n)
                break
            m = n // 2 - 1 if n % 2 == 0 else (n - 1) // 2
            p = next(q for q in prime_list if m < q <= 2 * m and q <= n - 2)
            parts.append(p)
            n -= p
        return parts

    for n in range(2, LIMIT + 1):
        parts = zerlege(n)
        assert sum(parts) == n
        assert all(is_prime[p] for p in parts), (n, parts)
        assert len(parts) <= math.floor(math.log2(n)) + 1, (n, parts)


if __name__ == "__main__":
    test_satz4_witnesses()
    test_methods_agree_N1000()
    test_sieve_counts()
    test_kette_primzahlen_und_luecken()
    test_bertrand_bis_100000()
    test_satz6_zerlegung_bis_5000()
    print("ALLE TESTS OK")
