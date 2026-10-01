# Hinweis zur Hardy–Littlewood-Normierung

Datei `singular_series_stichprobe.txt` vergleicht das **ungeordnete** \(G_2(n)\) mit
\[
S(n)\frac{n}{(\log n)^2},\qquad
S(n)=2\prod_{p>2}\Bigl(1-\frac{1}{(p-1)^2}\Bigr)\prod_{\substack{p\mid n\\ p>2}}\frac{p-1}{p-2}.
\]
Diese \(S(n)\)-Konvention gehört in der Literatur typischerweise zum **geordneten** Zählproblem ungerader Primzahlpaare.

**Erwartung:** \(G_2(n) \approx \tfrac12 S(n) n/(\log n)^2\) für große \(n\), plus Randterme (\(p=q\), \(p=2\)).  
Die gemessenen Verhältnisse \(0.6\)–\(0.76\) bei \(n=10^3\) und \(\approx 0.63\) bei \(n\approx 3\cdot 10^4\) sind daher **kein** Widerspruch zur Heuristik, sondern ein Faktor-\(\approx 2\)-Effekt plus Approximationsfehler des Produkts und des \(\log n\)-Hauptterms bei mäßigem \(n\).

Kleine \(n\) (\(12,30\)) sind für Asymptotik wertlos; sie stehen nur zur Nachvollziehbarkeit der Implementierung.

**Status:** Heuristik, **kein Satz**.
