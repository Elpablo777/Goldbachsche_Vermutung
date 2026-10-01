# Die binäre Goldbach-Aussage: Status, Teilergebnisse und eine endliche Verifikation

**Dokumenttyp:** Forschungsnotiz / Preprint-Entwurf dieses Archivs  
**Datum:** 29. September 2026  
**Lizenz:** CC BY-NC-SA 4.0  
**Beweisstatus von Satz 1 unten:** **offen** (Vermutung; hier nicht bewiesen)

---

## Abstract

We record the binary Goldbach statement in standard form and separate it from theorems that are actually proved: Vinogradov’s theorem, Chen’s theorem, and Helfgott’s theorem on the ternary problem. We report a reproducible verification of Goldbach’s binary statement for all even \(n\) with \(4\le n\le 200000\), and we explain why the circle method and sieve methods as presently known do not yield a proof for all even \(n\). No claim is made that the binary conjecture is proved.

Wir halten die binäre Goldbach-Aussage in Standardform fest und trennen sie von bewiesenen Sätzen (Vinogradov, Chen, Helfgott). Wir berichten eine reproduzierbare Prüfung für alle geraden \(n\in[4,200000]\) und benennen die Lücke der Kreismethode und der Siebmethoden. **Es wird nicht behauptet, die binäre Vermutung sei bewiesen.**

## 1. Introduction

Let \(\mathbb{P}\) be the set of primes. Goldbach’s binary conjecture asserts that every even integer \(n\ge 4\) is of the form \(p+q\) with \(p,q\in\mathbb{P}\). The ternary (weak) form asserts that every odd integer \(n\ge 7\) is a sum of three primes.

The ternary statement is a theorem of Helfgott [Hel13, Hel15], completing a line from Hardy–Littlewood [HL23] and Vinogradov [Vin37]. The binary statement remains open. Almost all even integers are sums of two primes [Est38, MV75]. The strongest classical sieve approximation is Chen’s theorem [Che66, Che73]; an explicit form is \(p+P_2\) for even \(N>\exp(\exp(32.7))\) [BJS22]. Exhaustive computation confirms the binary statement up to \(4\cdot 10^{18}\) [OHP14].

This note does **not** prove the binary conjecture. Its purpose is an auditable research record: definitions, citations, methods, a small independent computation, and an explicit gap analysis.

## 2. Preliminaries

**Conjecture 1 (binary Goldbach, \(G_{\mathrm{bin}}\)).**  
Every even integer \(n\ge 4\) is a sum of two primes.

**Theorem A (ternary Goldbach; Helfgott).**  
Every odd integer \(n\ge 7\) is a sum of three primes.  
*We do not reproduce the proof; we cite [Hel13, Hel15].*

**Theorem B (Vinogradov).**  
There exists \(C\) such that every odd integer \(n>C\) is a sum of three primes [Vin37].

**Theorem C (Chen).**  
Every sufficiently large even integer is the sum of a prime and an integer with at most two prime factors [Che73].

**Proposition 1 (elementary implication).**  
\(G_{\mathrm{bin}}\) implies the ternary statement for \(n\ge 7\). The converse is false on formal grounds (parity of the number of odd summands).

## 3. Results of this repository

**Proposition 2 (finite check, this work).**  
Every even integer \(n\) with \(4\le n\le 200000\) is a sum of two primes.

*Proof (complete, finite).* Let \(N=200000\). Compute the characteristic function of primes on \(\{0,\ldots,N\}\) by the sieve of Eratosthenes. For each even \(n\in[4,N]\) search for a prime \(p\le n/2\) such that \(n-p\) is marked prime. The implementation `06_verifikation/goldbach_check.py` reports \(99999\) even integers, \(0\) failures, \(\pi(N)=17984\), and maximal least summand \(383\). This is a finite inspection of a finite set; it is a proof of Proposition 2 and of nothing stronger. \(\square\)

**Remark (literature check).** Oliveira e Silva–Herzog–Pardi [OHP14] extend the same logical pattern to \(N=4\cdot 10^{18}\). We did not rerun that computation.

**Proposition 3 (independent finite check).** Same interval as Proposition 2, verified by set-membership (`goldbach_check_set.py`): \(99999\) even \(n\), \(0\) failures, same maximal least summand \(383\). Agreement of methods A and B on \(N=1000\) is asserted by `test_goldbach.py`.

**Proposition 4 (hand proof).** Every even \(n\) with \(4\le n\le 30\) is a sum of two primes; explicit partitions and primality checks are in `01_problemstellung/ELEMENTARE_SAETZE.md`.

## 4. Non-results (gaps)

**No theorem in this note implies Conjecture 1.**

On the major arcs, the circle method produces a main term of Hardy–Littlewood type involving the singular series
\[
S(n)=2\prod_{p>2}\Bigl(1-\frac{1}{(p-1)^2}\Bigr)\prod_{\substack{p\mid n\\p>2}}\frac{p-1}{p-2}.
\]
On the minor arcs the binary generating function \(S(\alpha)^2\) is not known to be small enough, unconditionally, to keep the remainder below the main term for every large even \(n\). The ternary problem has an extra factor \(S(\alpha)\) and is therefore accessible [Vin37, Hel13]. Chen’s sieve stops at \(P_2\).

A numerical comparison of unordered representation counts \(G_2(n)\) with \(S(n)n/(\log n)^2\) is recorded in `04_rechnungen/`; because \(G_2\) is unordered, ratios near \(1/2\) are expected and **do not** prove the asymptotic.

## 5. Methods not selected

See `03_methoden/METHODENKATALOG.md`: induction, naive use of the prime number theorem, bounded prime gaps, and unrefereed “proofs” of Conjecture 1 are rejected with explicit reasons.

## 6. Conclusion

Conjecture 1 remains open. Theorems A–C and Proposition 2 are the settled pieces recorded here. Any future claim of a proof of Conjecture 1 must close the minor-arc (or the \(P_2\to P_1\)) gap uniformly for all large even \(n\) and supply an explicit remaining finite range.

## References

- [Che66] J.-R. Chen, Kexue Tongbao 11 (1966), 385–386.  
- [Che73] J.-R. Chen, Sci. Sinica 16 (1973), 157–176.  
- [Hel13] H. A. Helfgott, arXiv:1312.7748.  
- [Hel15] H. A. Helfgott, arXiv:1501.05438.  
- [HL23] G. H. Hardy, J. E. Littlewood, Acta Math. 44 (1923), 1–70.  
- [OHP14] T. Oliveira e Silva, S. Herzog, S. Pardi, Math. Comp. 83 (2014), 2033–2060.  
- [Vin37] I. M. Vinogradov, Dokl. Akad. Nauk SSSR 15 (1937), 169–172.  
- [Est38] T. Estermann, Proc. London Math. Soc. (2) 44 (1938), 307–314.  
- [MV75] H. L. Montgomery, R. C. Vaughan, Acta Arith. 27 (1975), 353–370.  
- [BJS22] M. Bordignon, D. R. Johnston, V. Starichkova, arXiv:2207.09452.
