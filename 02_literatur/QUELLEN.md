# Literatur

Zitierregel: Nur Quellen, die in dieser Sitzung per Suche/Fetch getroffen oder klassisch kanonisch sind. Keine erfundenen Seitenzahlen.  
„Folgt / folgt nicht” ist die für Gegenagenten entscheidende Spalte.

**Update-Dateien (2026-10-01, primärquellengeprüft):**
- `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md` — KI/LLM-Stand (G_bin nicht angegangen), Lean-4-Formalisierung der ternären Vermutung, GitHub-Actions-Limits, primesieve, Pintz δ=0,28, Chen v6 „to appear IJNT”.
- `02_literatur/UPDATE_2026-10.md` — Verifikationsrekord-Details (Double-Check bis 4·10^17, 781,8 CPU-Jahre), Helfgott-Bandstatus (AMS 203, Druck ungeklärt), Ramaré–Saouter-Rolle (JNT 98 (2003)), behauptete Beweise 2024–2026: keiner anerkannt.

## A. Primärquellen zur binären Verifikation

1. Tomás Oliveira e Silva, Siegfried Herzog, Silvio Pardi.  
   *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to \(4\cdot 10^{18}\)*.  
   Mathematics of Computation **83** (2014), 2033–2060.  
   DOI-Pfad AMS: https://www.ams.org/journals/mcom/2014-83-288/S0025-5718-2013-02787-1/S0025-5718-2013-02787-1.pdf  
   **Folgt:** \(G_{\mathrm{bin}}\) gilt für alle geraden \(n\le 4\cdot 10^{18}\) (computergeprüft). Zusätzlich: mit Ramarè–Saouter folgt eine Schranke für die *ungerade* Goldbach-Aussage bis \(8.37\cdot 10^{26}\) (laut Abstract).  
   **Folgt nicht:** \(G_{\mathrm{bin}}\) für alle \(n\).

2. Tomás Oliveira e Silva. Projektdokumentation.  
   https://sweet.ua.pt/tos/goldbach.html  
   **Folgt:** Unabhängige Beschreibung desselben Rechenprojekts (u. a. Erreichen von \(4\cdot 10^{18}\) im April 2012; Double-Check bis \(4\cdot 10^{17}\) zum damaligen Stand der Seite).  
   **Folgt nicht:** mathematischer Beweis.

## B. Ternäre Goldbach

3. I. M. Vinogradov.  
   *Representation of an odd number as a sum of three primes.*  
   Dokl. Akad. Nauk SSSR **15** (1937), 169–172.  
   **Folgt:** \(G_{\mathrm{ter}}\) für alle ungeraden \(n>C\) mit (ursprünglich ineffektiver bzw. astronomischer) Konstante \(C\).  
   **Folgt nicht:** \(G_{\mathrm{bin}}\); folgt nicht \(G_{\mathrm{ter}}\) für alle ungeraden \(n\) ohne explizite \(C\) plus Check.

4. Harald A. Helfgott.  
   *The ternary Goldbach conjecture is true.* arXiv:1312.7748.  
   https://arxiv.org/abs/1312.7748  
   **Folgt (laut Arbeit):** jedes ungerade \(n\ge 7\) ist Summe dreier Primzahlen, durch analytische Schranken für große \(n\) plus Computerverifikation darunter (in Kombination mit Platt sowie der binären Prüfung bis \(4\cdot 10^{18}\)).  
   **Folgt nicht:** \(G_{\mathrm{bin}}\). Helfgott merkt explizit an, dass die starke Vermutung out of reach bleibt.

5. Harald A. Helfgott.  
   *The ternary Goldbach problem.* arXiv:1501.05438.  
   https://arxiv.org/abs/1501.05438  
   Buchlange Ausarbeitung; Annahme zur Publikation in *Annals of Mathematics Studies* (2015) ist in der Sekundärdiskussion belegt, die gedruckte Endfassung kann später liegen. Gegenagenten sollen die arXiv-Version als arbeitendes Referenzmanuskript nehmen.

## C. Siebmethoden / binäre Approximation

6. Jing-Run Chen.  
   Ankündigung: *Kexue Tongbao* **11** (1966), 385–386.  
   Ausführlich: *On the representation of a larger even integer as the sum of a prime and the product of at most two primes.* Scientia Sinica **16** (1973), 157–176.  
   **Folgt:** jedes hinreichend große gerade \(N\) ist \(p+P_2\) (Primzahl plus höchstens zwei Primfaktoren).  
   **Folgt nicht:** \(p+p'\).

7. P. M. Ross. Vereinfachung von Chens Beweis, 1975 (in der Chen-Theorem-Literatur standardzitiert).  
   **Folgt:** Exposition, kein stärkeres Goldbach.

8. A. Rényi. Gerade Zahl = Primzahl + fastprim mit beschränkter Faktorzahl (1947/48).  
   **Folgt:** Vorstufe zu Chen mit größerem \(K\).

## C2. Explizites Chen und „fast alle“

13. Theodor Estermann. *On Goldbach's problem: proof that almost all even positive integers are sums of two primes.* Proc. London Math. Soc. (2) **44** (1938), 307–314.  
    https://doi.org/10.1112/plms/s2-44.4.307  
    **Folgt:** \(E(X)=o(X)\) (Ausnahmemenge der geraden Nicht-Goldbach-Zahlen). Unabhängig parallel: Chudakov, van der Corput.  
    **Folgt nicht:** \(E(X)=0\).

14. H. L. Montgomery, R. C. Vaughan. *The exceptional set in Goldbach’s problem.* Acta Arithmetica **27** (1975), 353–370.  
    **Folgt (kanonische Aussage, hier über Fach-Sekundärquellen bestätigt):** \(E(X)\ll X^{1-\delta}\) für ein \(\delta>0\).  
    **Folgt nicht:** \(G_{\mathrm{bin}}\). Gegenagenten: Original in Acta Arith. gegenlesen.

15. Tomohiro Yamada. *Explicit Chen’s theorem.* arXiv:1511.03409.  
    **Anspruch:** \(p+P_2\) für gerade \(N>\exp\exp 36\).  
    **Vorsicht:** Bordignon–Johnston–Starichkova (nächster Eintrag) berichten Lücken; nicht als alleinige explizite Quelle verwenden.

16. Matteo Bordignon, Daniel R. Johnston, Valeriia Starichkova. *An explicit version of Chen’s theorem.* arXiv:2207.09452.  
    https://arxiv.org/abs/2207.09452  
    **Folgt (laut Arbeit):** jedes gerade \(N>\exp(\exp(32.7))\) ist \(p+P_2\); jedes gerade \(N\ge 4\) ist Primzahl plus Produkt von \(\le e^{29.3}\) Primzahlen.  
    **Folgt nicht:** \(p+p'\).

17. Olivier Ramaré. Every even integer is a sum of at most six primes (1995; Standardzitat der Goldbach-Übersichten).  
    **Folgt:** 6-Primzahl-Satz. Mit Helfgott: höchstens 4 Primzahlen für gerade \(n\ge 8\) (siehe `01_problemstellung/ELEMENTARE_SAETZE.md` Satz 3).  
    **Folgt nicht:** zwei Primzahlen.

## D. Kreismethode / Heuristik

9. G. H. Hardy, J. E. Littlewood.  
   *Some problems of ‘Partitio Numerorum’; III: On the expression of a number as a sum of primes.* Acta Math. **44** (1923), 1–70.  
   **Folgt:** asymptotische *Vermutung* für \(r_2(n)\) via singulärer Reihe; unter GRH-artigen Hypothesen Teilresultate.  
   **Folgt nicht:** unbedingter Beweis von \(G_{\mathrm{bin}}\).

## E. Sekundär / vorsichtig zitiert

10. Wikipedia *Chen's theorem*, *Goldbach's weak conjecture* — nur zur Navigation, nie als Beweisquelle.

11. Medium/Gridbach-Anspruch \(4\cdot 10^{18}+7\cdot 10^{13}\) (2024-er Popularbericht).  
    **Status in diesem Archiv:** nicht peer-reviewed; **nicht** als kanonische Schranke verwendet.

12. arXiv:2603.07850 (GPU-Verifikationsarchitektur, Preprint).  
    **Folgt:** bestätigt in der Einleitung den akademischen Rekord \(4\cdot 10^{18}\) als Benchmark; eigener Hardware-Ansatz.  
    **Folgt nicht:** Ersatz für Oliveira e Silva et al. ohne unabhängige Replikation.

## F. Was absichtlich fehlt

Es gibt Dutzende Preprints, die \(G_{\mathrm{bin}}\) „beweisen“. Ohne Annahme in einem referierten Zahlentheorie-Journal und ohne von der Fachgemeinschaft getragene Lückenfreiheit werden sie hier **nicht** als Lösung geführt. Gegenagenten: solche Preprints in `05_beweisentwuerfe/` unter „unzulässige Kurzbeweise“ ablegen, nicht in den Theorem-Teil.
