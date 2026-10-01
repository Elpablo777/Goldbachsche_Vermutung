# Exceptional Set und „fast alle“ geraden Zahlen

**Nicht** \(G_{\mathrm{bin}}\). Hier: was über die **Ausnahmemenge** bewiesen ist.

Sei \(E(X)\) die Anzahl der geraden \(n\le X\), die **keine** Goldbach-Partition besitzen.

## Sätze (Literatur)

1. **Chudakov (1937/38), van der Corput (1937), Estermann (1938).**  
   Fast alle geraden positiven ganzen Zahlen sind Summe zweier Primzahlen: \(E(X)=o(X)\), genauer der Anteil der darstellbaren geraden Zahlen unter den geraden Zahlen \(\le X\) geht gegen \(1\).  
   Estermann: *Proc. London Math. Soc.* (2) **44** (1938), 307–314.  
   DOI: https://doi.org/10.1112/plms/s2-44.4.307

2. **Montgomery–Vaughan (1975).**  
   Es gibt \(\delta>0\) mit \(E(X)\ll X^{1-\delta}\).  
   H. L. Montgomery, R. C. Vaughan, *The exceptional set in Goldbach’s problem*, Acta Arith. **27** (1975), 353–370.  
   (Standardzitat der Goldbach-Literatur; Websuche in dieser Sitzung bestätigte die Aussage über Sekundärquellen, das Original ist Acta Arithmetica.)

3. **Was das nicht ist.**  
   \(E(X)=o(X)\) erlaubt immer noch unendlich viele Gegenbeispiele. Selbst \(E(X)\ll X^{1-\delta}\) schließt \(G_{\mathrm{bin}}\) nicht. Nur \(E(X)=0\) für große \(X\) (plus endlicher Check) wäre \(G_{\mathrm{bin}}\).

## Beziehung zum Minor-Arc-Problem

„Almost all“ entsteht, weil man in \(X\) mitteln darf: große Werte von \(|S(\alpha)|\) auf Minor Arcs dürfen eine dünne Menge gerader \(n\) verderben. \(G_{\mathrm{bin}}\) verlangt **jedes** \(n\), also Kontrolle ohne Mittelung.

## Explizites Chen (nicht \(p+p'\))

- Yamada, arXiv:1511.03409: \(p+P_2\) für gerade \(N>\exp\exp 36\); spätere Arbeiten merken Lücken in der Ausführung an.
- Bordignon–Johnston–Starichkova, arXiv:2207.09452: jede gerade Zahl \(>\exp(\exp(32.7))\) ist \(p+P_2\) (explizite Version; die Autoren kritisieren Yamada).  
  Zusätzlich: jedes gerade \(N\ge 4\) ist Primzahl plus Produkt von höchstens \(e^{29.3}\) Primzahlen.

Diese Schranken sind astronomisch und **ersetzen** weder den Check bis \(4\cdot 10^{18}\) noch einen Beweis von \(G_{\mathrm{bin}}\).
