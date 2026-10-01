# Lückenanalyse — warum hier kein Beweis von \(G_{\mathrm{bin}}\) steht

## 0. Regel

Ein Entwurf darf `QED` nur tragen, wenn jede Quantorenschicht geschlossen ist.  
Dieser Datei ist **kein QED** zugeordnet.

## 1. Was ein vollständiger Beweis leisten müsste

Sei \(n\) gerade, \(n\to\infty\). Man muss \(r_2(n)>0\) zeigen (oder \(G_2(n)\ge 1\)).  
Zwei Standardstrategien:

### A. Analytisch (Kreismethode)

Zeige
\[
r_2(n)=\mathfrak{S}(n)\, \mathfrak{M}(n)+E(n)
\]
mit Hauptterm \(\mathfrak{M}(n)\asymp n/(\log n)^2\) (oder gewichtet \(\asymp n\)) und \(|E(n)|=o(\text{Hauptterm})\) **gleichmäßig in allen geraden** \(n\ge n_0\), plus explizites \(n_0\) plus Check \(n<n_0\).

**Lücke:** \(|E(n)|\) aus den Minor Arcs ist in der unbedingten Theorie nicht \(o(\text{Hauptterm})\) für das *binäre* Moment \(S^2\). Die ternäre Rettung \(|S|^3\) fehlt.

### B. Sieb

Zeige, dass \(\{n-p: p\in\mathbb{P},\, 2<p<n\}\) mindestens eine Primzahl enthält.

**Lücke:** Chen zeigt ein \(P_2\). Der Übergang \(P_2\to P_1\) erfordert, den Beitrag der Semiprime \(p_1 p_2\) vollständig nach unten gegen 0 zu drücken oder anders zu identifizieren — das ist genau das ungelöste Restproblem.

## 2. Beliebte Scheinargumente (verworfen)

| Argument | Bruchstelle |
|---|---|
| Induktion: gilt für \(n\), also für \(n+2\) | Es gibt keine kanonische Abbildung von Partitionen von \(n\) auf Partitionen von \(n+2\). |
| „Primzahlsatz \(\Rightarrow\) genug Kandidaten“ | Der Primzahlsatz zählt *unabhängig* in \([1,n]\) und \([1,n]\); die *Korrelation* \(1_{\mathbb{P}}(p)1_{\mathbb{P}}(n-p)\) ist das Problem (singuläre Reihe, Paritäten, Sieblevel). |
| „Dirichlet in der Progression \(n-p\)“ | \(p\) läuft über Primzahlen, nicht über ein festes Modul-System mit fester Differenz. |
| „Helfgott + \(n=(n-3)+3\)“ | Liefert drei Primzahlen für *ungerade* Ziele, nicht zwei für *gerade* Ziele. Für gerade \(m=p+q+r\) bräuchte man eine gerade Anzahl von Ungeraden — drei Ungerade sind ungerade. |
| Computer bis \(10^{18}\) plus „wird schon so weitergehen“ | Kein Deduktionsschritt. |
| Unreferierte 5-Seiten-Preprints | Werden erst nach lückenfreier Prüfung zitiert; bis dahin: nicht verwendet. |

## 3. Alternative nicht gewählte Rechenwege (bewusst offen gelassen)

1. **Explizite Formel / Weil-Explizite Formel** für \(\psi\) in \(n-p\): führt auf Nullstellen von \(L\)-Funktionen; ohne RH/GRH plus Nullstellenabstände keine gleichmäßige Positivität.
2. **Kreisproblem-Analog** in der Ebene (Gitterpunkte auf \(x+y=n\) im Primzahlgitter): gleichwertig zu \(G_{\mathrm{bin}}\).
3. **Additive Kombinatorik / transference (Green–Tao-Stil)**: mächtig für lineare Gleichungen in dichten positiven-oberen-Dichte-Mengen; die Primzahlen in \([1,n]\) haben Dichte \(1/\log n\), und die Goldbach-Gleichung ist eine *binäre* Gleichung — transference liefert hier historisch keine Lösung von \(G_{\mathrm{bin}}\).
4. **Harmonische Analyse auf \(\mathbb{Z}/N\mathbb{Z}\)** mit großen Spektren: verwandt mit Minor Arcs.

Diese Wege sind **nicht** deshalb falsch, weil sie hier nicht zu Ende geführt wurden; sie sind die offenen Forschungsfronten.

## 4. Was *bewiesen* weiterverwendet werden darf

- \(G_{\mathrm{ter}}\) (Helfgott, Literatur).  
- Chen \(p+P_2\) (Literatur).  
- Vinogradov für große ungerade \(n\) (Literatur).  
- Endliche Checks, *sofern* das Intervall und der Algorithmus angegeben sind.

Nichts davon ist \(G_{\mathrm{bin}}\) für alle geraden \(n\ge 4\).
