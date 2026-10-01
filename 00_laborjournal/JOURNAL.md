# Laborjournal

Format jeder Eintragung: Zeit (ISO, lokale Sitzung), Aktion, Methode, Ergebnis, nächster Schritt.  
Andere Agenten dürfen Einträge nur **anhängen**, nicht stumm überschreiben.

---

## 2026-09-29 — Start des Archivs

**Recherche**

- Websuche nach Verifikationsschranke, Helfgott, Chen.
- Primärseiten:
  - Oliveira e Silva, Projektseite: https://sweet.ua.pt/tos/goldbach.html
  - Oliveira e Silva, Herzog, Pardi, *Math. Comp.* 83 (2014), 2033–2060, PDF AMS: https://www.ams.org/journals/mcom/2014-83-288/S0025-5718-2013-02787-1/S0025-5718-2013-02787-1.pdf
  - Helfgott, *The ternary Goldbach conjecture is true*, arXiv:1312.7748 — https://arxiv.org/abs/1312.7748
  - Helfgott, *The ternary Goldbach problem*, arXiv:1501.05438 — https://arxiv.org/abs/1501.05438
  - Chen-Theorem: Chen, *Sci. Sinica* 16 (1973), 157–176; Ankündigung *Kexue Tongbao* 11 (1966).

**Analyse (Literatur, nicht eigene Erfindung)**

- Binäre Goldbach: fachlich unbewiesen.
- Anerkannte exhaustive CPU-Verifikation: alle geraden \(n \le 4\cdot 10^{18}\).
- Ternäre (schwache) Form: Helfgott 2013, Aufbau auf Vinogradov + explizite Major/Minor-Arcs + Computerchecks; Manuskript u. a. für *Annals of Mathematics Studies* akzeptiert (2015), Überarbeitung öffentlich über arXiv.
- Chen: \(n = p + P_2\) für große gerade \(n\); das ist **nicht** \(p+p'\).

**Nicht gewählte / verworfene Kurzschlüsse**

- „Aus Helfgott folgt binäres Goldbach“ — **falsch**. Helfgott selbst: die starke Vermutung bleibt out of reach.
- „Aus Chen folgt Goldbach, weil \(P_2\) oft prim ist“ — **unbewiesen**.
- „Endliche Prüfung bis \(N\) plus Heuristik = Beweis“ — **unzulässig**.
- Gridbach/Medium-Claims über \(4\cdot 10^{18}+7\cdot 10^{13}\): **nicht** als peer-review-äquivalenten Rekord geführt (nur notiert).

**Rechnung / Prüfung (dieses Repo)**

- Methode: Sieb des Eratosthenes bis \(N=200000\), für jedes gerade \(n\) kleinstes \(p\le n/2\) mit \(n-p\) prim.
- Kommando: `python 06_verifikation/goldbach_check.py 200000`
- Ergebnis: 99999 Werte, 0 Fehlschläge, \(\pi(200000)=17984\), max. minimales \(p(n)=383\), Laufzeit \(\approx 0.465\,\mathrm{s}\), Python 3.14.7.
- Hardy–Littlewood-Stichprobe: ungeordnetes \(G_2(n)\) gegen den **geordneten** Hauptterm \(S(n)\, n/(\log n)^2\) → Verhältnisse \(\approx 0.19\)–\(0.76\); das ist ein **Normierungseffekt** (Faktor \(\approx 1/2\) plus kleine-\(n\)-Fehler), kein Gegenbeispiel zur Heuristik.

**Hintergrundagenten**

- Zwei Cursor-Subagenten scheiterten am Free-Plan-Limit für benannte Modelle; die Arbeit wurde deshalb lokal in diesem Ordner fortgesetzt.

**Nächster Schritt (Stand nach v0)**

- Lücken der Kreismethode im binären Fall sauber aufschreiben; keine Behauptung eines vollständigen Beweises.

---

## 2026-09-29 — Vertiefung (v1)

**Anlass:** Goal-Fortsetzung. Hintergrundagenten weiter am Free-Plan-Limit gescheitert; Arbeit lokal.

**Recherche**

- Estermann 1938, DOI 10.1112/plms/s2-44.4.307: almost all even integers.
- Montgomery–Vaughan, *Acta Arith.* 27 (1975): \(E(X)\ll X^{1-\delta}\) (Aussage über Sekundärquellen bestätigt; Original nicht Blatt für Blatt gelesen).
- Yamada arXiv:1511.03409: \(\exp\exp 36\); Kritik und Ersatz: Bordignon–Johnston–Starichkova arXiv:2207.09452, Schranke \(\exp(\exp(32.7))\).
- Helfgott ICM-Notiz (1404.2224): Chudakov / van der Corput / Estermann unabhängig 1937–38.

**Neue geschlossene Beweise (hier)**

- `01_problemstellung/ELEMENTARE_SAETZE.md`: Sätze 1–4 vollständig ausgeschrieben.

**Zweite Rechnung**

- `python 06_verifikation/goldbach_check_set.py 200000`: 99999, 0 Fehlschläge, max. min. \(p=383\), \(\approx 0.098\,\mathrm{s}\).
- `python 06_verifikation/test_goldbach.py`: ALLE TESTS OK (Satz-4-Partitionen, A=B auf \(N=1000\), \(\pi(200000)=17984\)).

**Analyse**

- Almost-all schließt \(G_{\mathrm{bin}}\) nicht (unendlich viele Ausnahmen möglich).
- Explizites Chen bleibt \(p+P_2\) mit astronomischer Schwelle.

**Nächster Schritt**

- Acta-Arithmetica-Original für Montgomery–Vaughan; \(G_{\mathrm{bin}}\) weiter offen.

---

## 2026-10-01 — Repository-Erstellung und Ausbau geplant (v2)

**Aktion**

- GitHub-Repository angelegt: https://github.com/Elpablo777/Goldbachsche_Vermutung (öffentlich, damit Gegenprüfungs-Agenten ohne Zugangshürde lesen können; Umschalten auf privat jederzeit möglich).
- Lokales Git initialisiert (`main`), erste Push folgt unmittelbar; Beschreibung und Topics am Repo gesetzt.
- `.gitignore`: `__pycache__`, Go-Buildartefakte und große regenerierbare Witness-`.bin`-Dateien werden nicht gepusht (regenerierbar, siehe `06_verifikation/ANLEITUNG.md`).

**Hinweis zur Zielsetzung (Ehrlichkeitsregel bleibt)**

- Auftrag: „löse die Goldbachsche Vermutung, keine Vermutung, sondern Lösung“. Stand der Fachgemeinschaft (und dieses Archivs): die binäre Goldbachsche Vermutung ist **offen**. Archivregeln verbieten Scheinbeweise; es wird weiter nur Bewiesenes, endliche Verifikation und klar markierte Heuristik getrennt.
- „255 runs“ im Auftrag: als „nutze die verfügbaren Rechen-/Agentenläufe“ interpretiert; Zahl inhaltlich unklar, im Journal notiert statt still interpretiert.

**Gestartete Arbeiten (Sitzung 2026-10-01)**

- Hintergrundagent Literatur-Update (Stand Okt. 2026): Verifikationsrekord, Ausnahmemengen-Exponent, explizites Chen, Helfgott-Publikationsstatus, behauptete Beweise 2024–2026. Ergebnis landet als `02_literatur/UPDATE_2026-10.md`.
- Geplant und angestoßen:
  - Methode C (NumPy, vektorisiert) als dritte, strukturell unabhängige Prüfung bis \(N=10^7\).
  - Methode D (Go, eigene Sprache/Implementierung, ungerades Bitsieb) bis \(N=10^8\), mit Witness-Datei (minimales \(p(n)\) je geradem \(n\)) und unabhängigem Python-Verifier als Cross-Check.
  - Statistik: maximale minimale Summandenprimzahl \(p(n)\) mit Rekordhaltern, Goldbach-Komet-Stichprobe mit korrigierter \(\tfrac12 S(n) n/(\log n)^2\)-Normierung.
  - Neue elementare Sätze (Bertrand per Erdős-Beweis; daraus Zerlegung jeder ganzen Zahl \(n\ge2\) in höchstens \(O(\log n)\) Primzahlen) lückenlos in `01_problemstellung/ELEMENTARE_SAETZE.md`.
- **Zielpause:** die Sitzung wurde zwischenzeitlich vom Nutzer pausiert; Facharbeit wird nach Freigabe fortgesetzt. Repo-Inhalt wird nach jedem Meilenstein commit+push gehalten.

**Nächster Schritt**

- Push des Archivs v2; danach Fortsetzung der Rechenläufe und Dokumentation wie oben.
