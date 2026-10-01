# Elementare Sätze mit vollständigem Beweis

Diese Datei enthält **nur** Aussagen, deren Beweis hier lückenlos steht.  
\(G_{\mathrm{bin}}\) kommt nur als *Hypothese* in Satz 2 vor, nicht als bewiesener Satz.

**Satz 1.** \(4 = 2+2\) mit \(2\in\mathbb{P}\).  
*Beweis.* Die Zahl \(2\) ist prim (einzige gerade Primzahl; die einzigen positiven Teiler sind \(1\) und \(2\)). Addition in \(\mathbb{Z}\) ergibt \(4\). \(\square\)

**Satz 2 (bedingte Implikation).** Aus \(G_{\mathrm{bin}}\) folgt: jedes ungerade \(n\ge 7\) ist Summe dreier Primzahlen.  
*Beweis.* Sei \(n\ge 7\) ungerade. Dann ist \(n-3\) gerade und \(n-3\ge 4\). Nach \(G_{\mathrm{bin}}\) existieren \(p,q\in\mathbb{P}\) mit \(p+q=n-3\). Es ist \(3\in\mathbb{P}\), also \(n=3+p+q\). \(\square\)

**Satz 3 (keine Standardreduktion von ternär auf binär).** Sei \(N\ge 8\) gerade. Dann ist \(N-3\) ungerade und \(\ge 5\). Schreibt man \(N-3=p+q+r\) mit Primzahlen (ternäre Zerlegung), so folgt \(N=p+q+r+3\), also eine Darstellung als **vier** Primzahlen, nicht als zwei.  
*Beweis.* Gerade minus ungerade ist ungerade. Die Gleichung hat vier Summanden auf der rechten Seite. \(\square\)

**Folgerung (Literatur, hier nur zitiert, nicht neu bewiesen).** Aus Helfgotts ternärem Satz folgt, dass jedes gerade \(N\ge 8\) Summe von höchstens vier Primzahlen ist (Satz 3 mit \(N-3\ge 5\) ungerade \(\ge 7\) für \(N\ge 10\); \(N=8=3+5\) bzw. \(3+3+2\) separat). Das ist **schwächer** als \(G_{\mathrm{bin}}\).

**Satz 4 (endliche explizite Liste).** Jede gerade Zahl \(n\) mit \(4\le n\le 30\) ist Summe zweier Primzahlen, mit den Partitionen
\[
\begin{align*}
4&=2+2,&
6&=3+3,&
8&=3+5,&
10&=3+7,&
12&=5+7,\\
14&=3+11,&
16&=3+13,&
18&=5+13,&
20&=3+17,&
22&=3+19,\\
24&=5+19,&
26&=3+23,&
28&=5+23,&
30&=7+23.
\end{align*}
\]
*Beweis.* Jeder rechte Summand ist eine der Primzahlen \(2,3,5,7,11,13,17,19,23\), deren Primheit durch Teilerexhaustion bis zur Wurzel folgt (elementar, endlich viele Divisionen). Die Gleichheiten sind Dezimalarithmetik. \(\square\)

Satz 4 ist ein echter, vollständiger Beweis eines **endlichen** Spezialfalls von \(G_{\mathrm{bin}}\). Die Ausdehnung auf alle \(n\) fehlt.
