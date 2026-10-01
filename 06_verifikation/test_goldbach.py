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


if __name__ == "__main__":
    test_satz4_witnesses()
    test_methods_agree_N1000()
    test_sieve_counts()
    print("ALLE TESTS OK")
