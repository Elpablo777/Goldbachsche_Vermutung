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

---

# Ergänzt am 2026-10-01: Sätze 5–7

Die folgenden drei Sätze sind **vollständig elementar und bedingungslos bewiesen**.
Sie lösen \(G_{\mathrm{bin}}\) **nicht** (siehe die Einordnung am Ende).

**Hilfssatz A (Maximum unter den Binomialkoeffizienten).** Für \(n\ge1\) gilt
\(\binom{2n}{n}=\max_{0\le k\le 2n}\binom{2n}{k}\) und \(\sum_{k=0}^{2n}\binom{2n}{k}=4^{n}\); also
\(\binom{2n}{n}\ge 4^{n}/(2n+1)\).
*Beweis.* \(\binom{2n}{k+1}=\binom{2n}{k}\cdot\frac{2n-k}{k+1}\), und \(\frac{2n-k}{k+1}\ge1\iff k\le n-1\).
Die Folge \(\binom{2n}{k}\) steigt also bis \(k=n\) und fällt danach symmetrisch; das Maximum liegt bei \(k=n\). Der binomische Lehrsatz mit \(a=b=1\) liefert die Summe \(2^{2n}=4^{n}\). Da alle \(2n+1\) Summanden \(\le\binom{2n}{n}\) sind, folgt die Ungleichung. \(\square\)

**Hilfssatz B (Primzahlprodukt).** Sei \(P(n)=\prod_{p\le n}p\) für ganze \(n\ge1\) (\(P(1)=1\), leeres Produkt). Dann gilt:
(i) Für jedes \(m\ge1\): \(P(2m)\le P(m)\cdot\binom{2m}{m}<4^{m}\,P(m)\).
(ii) Für alle \(n\ge2\): \(P(n)<4^{\,n+2\lceil\log_{2}n\rceil}\).
*Beweis.*
(i) Jede Primzahl \(p\) mit \(m<p\le2m\) teilt \((2m)!\) genau einmal (denn \(2m<2p\)) und \(m!\) gar nicht; also ist \(\nu_p\!\bigl(\binom{2m}{m}\bigr)=1\). Da die Primzahlen paarweise verschieden sind, teilt ihr Produkt \(\prod_{m<p\le2m}p\) den Binomialkoeffizienten:
\(P(2m)=P(m)\cdot\prod_{m<p\le2m}p\le P(m)\binom{2m}{m}\). Und \(\binom{2m}{m}<4^{m}\), denn \(\sum_{k=0}^{2m}\binom{2m}{k}=4^{m}\) mit \(2m\) weiteren positiven Summanden neben dem Maximum \(\binom{2m}{m}\) (Hilfssatz A).
(ii) Induktion über \(n\). Basis \(n=2\): \(P(2)=2<4^{4}\). Schritt: Sei \(m=\lceil n/2\rceil<n\) (für \(n\ge3\); \(m=1\) nur bei \(n=2\)). Wegen \(n\le2m\) und Monotonie von \(P\) sowie (i):
\(P(n)\le P(2m)<4^{m}P(m)\). Nach Induktionsvoraussetzung \(P(m)<4^{\,m+2\lceil\log_{2}m\rceil}\), also
\(P(n)<4^{\,2m+2\lceil\log_{2}m\rceil}\). Nun ist \(2m=2\lceil n/2\rceil\le n+1\), und es gilt \(\lceil\log_{2}m\rceil\le\lceil\log_{2}n\rceil-1\): denn mit \(k=\lceil\log_{2}n\rceil\) ist \(2^{k-1}<n\le2^{k}\), also \(m=\lceil n/2\rceil\le\lceil(2^{k}-1)/2\rceil=2^{k-1}\) (Fall \(n<2^{k}\)) bzw. \(m=2^{k-1}\) (Fall \(n=2^{k}\)). Somit
\(2m+2\lceil\log_{2}m\rceil\le(n+1)+2\lceil\log_{2}n\rceil-2=n+2\lceil\log_{2}n\rceil-1<n+2\lceil\log_{2}n\rceil\). \(\square\)

**Hilfssatz C (p-Valenz des zentralen Binomialkoeffizienten).** Sei \(p\) prim und
\(e_p:=\nu_p\!\bigl(\binom{2n}{n}\bigr)\). Dann
\(e_p=\sum_{j\ge1}\bigl(\lfloor 2n/p^{j}\rfloor-2\lfloor n/p^{j}\rfloor\bigr)\), jeder Summand ist \(0\) oder \(1\), und für \(p>\sqrt{2n}\) gilt \(e_p\le1\).
*Beweis.* Legendre: \(\nu_p(m!)=\sum_{j\ge1}\lfloor m/p^{j}\rfloor\) (die Vielfachen von \(p^{j}\) in \(1,\dots,m\) werden je \(m/p^{j}\)-fach gezählt, für jedes \(j\)). Wegen \(\binom{2n}{n}=(2n)!/(n!)^{2}\) folgt die Formel. Für reelles \(x\) ist \(\lfloor2x\rfloor-2\lfloor x\rfloor\in\{0,1\}\); jeder Summand ist also \(0\) oder \(1\), und Summanden mit \(p^{j}>2n\) verschwinden. Für \(p>\sqrt{2n}\) ist \(p^{2}>2n\), also bleibt nur \(j=1\): \(e_p\le1\). \(\square\)

**Satz 5 (Bertrandsches Postulat).** Für jede ganze Zahl \(m\ge1\) existiert eine Primzahl \(p\) mit \(m<p\le2m\).

*Beweis.* Die Fälle \(m=1\) (\(p=2\)) und \(m=2\) (\(p=3\)) sind direkt.

**Schritt 1 (analytischer Bereich \(n\ge8192\)).** Angenommen, für ein festes \(n\ge8192\) gibt es **keine** Primzahl in \((n,2n]\). Nach Fundamentalsatz und Hilfssatz C zerfällt \(\binom{2n}{n}=\prod_{p}p^{e_p}\), und wir abschätzen die Klassen:

1. \(p\le\sqrt{2n}\): Aus \(e_p\le\max\{j:p^{j}\le2n\}\le\log_{p}(2n)\) folgt \(p^{e_p}\le2n\). Die Anzahl dieser Primzahlen ist höchstens \(\lfloor\sqrt{2n}\rfloor-1<\sqrt{2n}\) (paarweise verschiedene ganze Zahlen \(\ge2\)). Beitrag: \(<(2n)^{\sqrt{2n}}\).
2. \(\sqrt{2n}<p\le2n/3\): \(e_p\le1\) (Hilfssatz C), also ist der Beitrag höchstens \(P(\lfloor2n/3\rfloor)<4^{\,\lfloor2n/3\rfloor+2\lceil\log_{2}\lfloor2n/3\rfloor\rceil}\le4^{\,2n/3+2\lceil\log_{2}(2n)\rceil}\) (Hilfssatz B(ii)).
3. \(2n/3<p\le n\): Dann ist \(2p\le2n<3p\), also \(\lfloor2n/p\rfloor=2\), und \(p<n<2p\), also \(\lfloor n/p\rfloor=1\); für \(j\ge2\) ist \(p^{j}>4n^{2}/9>2n\) (da \(n\ge5\)). Somit \(e_p=2-2\cdot1=0\): kein Beitrag.
4. \(n<p\le2n\): nach Annahme leer (sonst wäre ein solches \(p\) mit \(e_p=1\) Teiler von \(\binom{2n}{n}\)).

Also
\[
\binom{2n}{n}<4^{\,2n/3+2\lceil\log_{2}(2n)\rceil}\,(2n)^{\sqrt{2n}}=:U. \tag{1}
\]
Andererseits liefert Hilfssatz A \(\binom{2n}{n}\ge4^{n}/(2n+1)=:L\).

**Behauptung:** \(U\le L\) für \(n\ge8192\). Mit (1) und Hilfssatz A gälte dann \(\binom{2n}{n}<U\le L\le\binom{2n}{n}\) — Widerspruch; die Annahme wäre falsch.

Setze \(x=\sqrt{2n}\ (\ge128)\). Die Ungleichung \(U\le L\) ist äquivalent zu \(\tfrac{x^{2}}{6}\ge2x\log_{2}x+2\lceil2\log_{2}x\rceil+\log_{2}(x^{2}+1)\) und — nach Multiplikation beider Seiten mit \(2\) — äquivalent zu
\[
\frac{x^{2}}{3}\;\ge\;4x\log_{2}x\;+\;2\lceil2\log_{2}x\rceil\;+\;\log_{2}(x^{2}+1). \tag{2}
\]
Es genügt, die stärkere Ungleichung mit \(2\lceil2\log_{2}x\rceil\le4\log_{2}x+2\) zu zeigen:
\[
G(x):=\frac{x^{2}}{3}-4x\log_{2}x-4\log_{2}x-2-\log_{2}(x^{2}+1)\;\ge\;0\quad(x\ge128).
\]
Numerisch: \(G(128)=\tfrac{16384}{3}-3584-28-2-\log_{2}16385>5461{,}33-3584-28-2-14>1833>0\).
Für \(x\ge128\) ist
\(G'(x)=\tfrac{2x}{3}-4\log_{2}x-\tfrac{4}{\ln 2}-\tfrac{4}{x\ln2}-\tfrac{2x}{(x^{2}+1)\ln2}\).
Die Funktion \(h(x):=\tfrac{2x}{3}-4\log_{2}x\) ist auf \([128,\infty)\) wachsend (\(h'(x)=\tfrac23-\tfrac{4}{x\ln2}>0\) für \(x>6/\ln2\approx8{,}7\)), also \(h(x)\ge h(128)=\tfrac{256}{3}-28>57{,}3\). Die drei negativen Restglieder sind \(\le\tfrac{4}{\ln2}\approx5{,}78\), \(\le\tfrac{4}{128\ln2}<0{,}046\) und \(\le\tfrac{2}{128\ln2}<0{,}023\) (das letzte wegen \(\tfrac{x}{x^{2}+1}\le\tfrac1x\)). Somit \(G'(x)>57{,}3-5{,}78-0{,}046-0{,}023>51>0\): \(G\) ist auf \([128,\infty)\) streng wachsend, also \(G(x)\ge G(128)>0\). Das beweist (2) und damit den Widerspruch. Also existiert für jedes \(n\ge8192\) eine Primzahl in \((n,2n]\).

**Schritt 2 (endlicher Bereich \(1\le n<8192\) per Primzahlkette).** Betrachte die Primzahlen
\[
3,\;5,\;7,\;13,\;23,\;43,\;83,\;163,\;317,\;631,\;1259,\;2503,\;5003,\;8009,\;10007,
\]
\(p_1<\dots<p_{15}\). Ihre Primheit ist endlich durch Probedivision geprüft (z. B. \(10007\): \(\sqrt{10007}<101\), keine der Divisionen durch \(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97\) geht auf; die übrigen entsprechend, kleinere Teilermengen) — zusätzlich maschinell verifiziert in `06_verifikation/test_goldbach.py`. Es gilt \(p_{i+1}<2p_{i}\) für alle \(i\):
\(5<6,\;7<10,\;13<14,\;23<26,\;43<46,\;83<86,\;163<166,\;317<326,\;631<634,\;1259<1262,\;2503<2518,\;5003<5006,\;8009<10006,\;10007<16018\).

Sei \(3\le n<8192\) und \(i\) minimal mit \(p_i>n\) (existiert, da \(10007>8192>n\)). Dann ist \(p_{i-1}\le n\) (Minimalität von \(i\); für \(n=3\) ist \(p_{i-1}=p_1=3\le n\)), und
\(n<p_i<2p_{i-1}\le2n\), also \(p_i\in(n,2n]\). \(\square\)

**Bemerkung.** Die Schwelle \(8192\) ist bewusst konservativ gewählt (die Abschätzung trägt ab etwa \(n\approx3000\); exakte Optimierung war nicht das Ziel). Die Beweisstruktur folgt Erdős (1932; Darstellung u. a. in Aigner–Ziegler, *Proofs from THE BOOK*, Kap. 2); hier sind alle Schranken explizit ausgeschrieben, der Produkt-Schalter \(P(n)<4^{n+2\lceil\log_{2}n\rceil}\) (Hilfssatz B) ist mit Beweis versehen, und der endliche Rest ist per zertifizierter Primzahlkette plus Maschinencheck geschlossen.

**Satz 6 (schwache, elementare Zerlegungsaussage).** Jede ganze Zahl \(n\ge2\) ist Summe von höchstens \(\lfloor\log_{2}n\rfloor+1\) Primzahlen.

*Beweis.* Induktion über \(n\). Sei \(T(n)\) die Mindestanzahl von Primzahlen mit Summe \(n\).

*Basis:* \(n=2,3\): \(n\) ist prim, \(T(n)=1\le\lfloor\log_{2}n\rfloor+1\).

*Induktionsschritt (\(n\ge4\)); Voraussetzung: Behauptung für alle \(2\le n'<n\).*

- **\(n\) prim:** \(T(n)=1\le\lfloor\log_{2}n\rfloor+1\). \(\checkmark\)
- **\(n\) gerade:** Setze \(m=n/2-1\ge1\). Nach Satz 5 existiert eine Primzahl \(p\) mit \(m<p\le2m=n-2\). Wähle ein solches \(p\). Dann ist \(n':=n-p\) ganzzahlig mit \(2\le n'\le n/2\) (oben: \(p\le n-2\); unten: \(p\ge m+1=n/2\)). Nach Induktionsvoraussetzung ist \(n'\) Summe von höchstens \(\lfloor\log_{2}n'\rfloor+1\) Primzahlen, und
  \[
  T(n)\le1+T(n')\le1+\lfloor\log_{2}n'\rfloor+1\le1+\bigl(\lfloor\log_{2}n\rfloor-1\bigr)+1=\lfloor\log_{2}n\rfloor+1,
  \]
  wobei \(\lfloor\log_{2}n'\rfloor\le\lfloor\log_{2}n\rfloor-1\), weil \(n'\le n/2\) und \(n\) gerade (\(\log_{2}n'\le\log_{2}n-1\)).
- **\(n\) ungerade und nicht prim:** Dann ist \(n\ge9\). Setze \(m=(n-1)/2\ge4\). Nach Satz 5 existiert eine Primzahl \(p\) mit \((n-1)/2<p\le n-1\); \(p\) ist ungerade (\(p>2\)). Also ist \(n':=n-p\) gerade mit \(2\le n'\le(n-1)/2<n/2\). Wie oben:
  \[
  T(n)\le1+T(n')\le1+\lfloor\log_{2}n'\rfloor+1\le\lfloor\log_{2}n\rfloor+1,
  \]
  da \(n'<n/2\Rightarrow\log_{2}n'<\log_{2}n-1\Rightarrow\lfloor\log_{2}n'\rfloor\le\lfloor\log_{2}n\rfloor-1\) (aus \(a<b-1\) folgt \(\lfloor a\rfloor\le\lceil b-1\rceil-1\le\lfloor b\rfloor-1\) für reelle \(a,b\)). \(\square\)

**Beispiel (konstruktiv).** \(n=100\): \(m=49\), \(p=53\in(49,98]\), \(n'=47\) prim \(\Rightarrow100=53+47\) (2 Primzahlen). \(n=961=31^{2}\): \(m=479\), \(p=487\), \(n'=474=2\cdot237\)… Fortsetzung per Satz 6; der Algorithmus terminiert, da \(n'\le n/2\) in jedem Schritt.

**Satz 7 (Korrektheit des Eratosthenes-Siebs).** Sei \(N\ge2\) und werde das Sieb wie in `06_verifikation/goldbach_check.py` ausgeführt: Initialisiere \(b[x]=1\) für \(x\ge2\), \(b[0]=b[1]=0\); für \(i=2,3,\dots,\lfloor\sqrt N\rfloor\): falls \(b[i]=1\), setze \(b[j]=0\) für \(j=i^{2},i^{2}+i,i^{2}+2i,\dots\le N\). Dann gilt nach dem Lauf: \(b[x]=1\iff x\) prim.
*Beweis.*
(a) *Primzahlen bleiben markiert.* Angenommen, eine Primzahl \(q\) wird auf \(0\) gesetzt, beim Index \(i\) mit \(q\ge i^{2}\), \(i\mid q\). Da \(i\ge2\) und \(q\) prim ist, folgt \(i=q\); aber \(i\le\lfloor\sqrt N\rfloor<q\) für \(q>\sqrt N\), und für \(q\le\sqrt N\) ist \(i=q\) mit \(q\ge q^{2}\) falsch (\(q\ge2\)). Widerspruch in beiden Fällen; genauere Zerlegung: die Marke bei Index \(i\) trifft nur Vielfache \(j=i\cdot k\) mit \(k\ge i\ge2\), also zusammengesetzte \(j\). Eine Primzahl \(q\) ist kein solches Vielfaches. \(\checkmark\)
(b) *Zusammengesetzte \(x\le N\) werden markiert.* Sei \(x\) zusammengesetzt, \(p\) sein **kleinster** Primteiler, \(x=p\,k\). Da kein Primteiler von \(x\) kleiner als \(p\) ist, ist \(k\ge p\), also \(p^{2}\le x\le N\) und \(p\le\lfloor\sqrt N\rfloor\): der Index \(i=p\) wird ausgeführt. Beim Erreichen von \(i=p\) ist \(b[p]\) noch \(1\): wäre \(p\) vorher (durch ein \(i'<p\)) gelöscht worden, so gälte \(i'\mid p\) mit \(2\le i'<p\) — unmöglich, da \(p\) prim. Und \(x\ge p^{2}\), \(x\equiv0\pmod p\), also ist \(x\) genau eines der markierten \(j=p^{2},p^{2}+p,\dots\) (alle Vielfachen \(j\ge p^{2}\) mit \(p\mid j\) erscheinen, da die Schrittweite \(p\) ist und \(x-p\cdot t<p^{2}\) erst unterhalb startet). \(\checkmark\)
Aus (a)+(b) folgt die Behauptung. \(\square\)

**Bemerkung (ungerades Bitsieb, Methode D).** `06_verifikation/go/goldbach_check.go` siebt nur ungerade Zahlen (Bit \(i\) ↔ \(2i+1\)): die Markierung läuft über ungerade Vielfache \(m=p^{2},p^{2}+2p,\dots\) eines ungeraden \(p\) — das sind genau die ungeraden Vielfachen von \(p\) ab \(p^{2}\); gerade Vielfache sind durch die Sonderrolle der \(2\) abgedeckt. Die Korrektheit folgt wie in Satz 7.

**Einordnung (wichtig).** Satz 5 ist ein klassisches berühmtes Resultat (Bertrand 1845, Beweis Čebyšev 1852, obige Fassung Erdős 1932); Satz 6 ist eine **exponentiell schwächere** Zerlegungsaussage als die aus der Literatur bekannten (Ramaré: \(\le6\) Primzahlen für alle geraden \(n\); Helfgott ternär: \(\le4\) für gerade \(n\ge8\), siehe Folgerung nach Satz 3). **Keiner der Sätze 5–7 impliziert \(G_{\mathrm{bin}}\)**: Satz 6 zeigt nur Summen mit \(O(\log n)\) Summanden, nicht mit zwei. Ihr Wert hier: sie sind komplett, bedingungslos und auditierbar — im Gegensatz zur offenen Vermutung selbst.
