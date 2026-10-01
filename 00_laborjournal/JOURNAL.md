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
- Lokales Git initialisiert (`main`), Push erfolgreich; Topics gesetzt (goldbach-conjecture, number-theory, prime-numbers, mathematics, verification, reproducible-research, research); Beschreibung am Repo gesetzt.
- Betriebsnotiz für nachfolgende Agenten: Push mit der privaten Mailadresse `hannover84@msn.com` wird von GitHub abgelehnt (E-Mail-Privatsphäre). Im Repo ist deshalb lokal `user.email = 20980418+Elpablo777@users.noreply.github.com` gesetzt (GitHub-NoReply-Format). Nicht global ändern.
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

---

## 2026-10-01 — Meilenstein: Verifikation bis 10^8, vier Methoden, Witness-Cross-Check (v3)

**Neue Infrastruktur (alles in `06_verifikation/`)**

- Methode C `goldbach_check_np.py` (NumPy, vektorisiert): Restmengen-Elimination über k=n/2, minimaler Witness durch aufsteigende Primzahl-Pässe; „dead“-k sind nach Beweis im Dateikopf endgültige Fehlschläge (jede Primzahl ≤ k wurde getestet).
- Methode D `go/goldbach_check.go` (Go 1.27, vollständig unabhängig): ungerades Bitsieb (Bit i ↔ 2i+1), parallele Chunks, Witness-Datei im Format `GBWIT1` (LEB128 + CRC32).
- Verifier `verify_witnesses.py` (Python/NumPy, unabhängig von D): CRC, Header, JEDES Witness (p prim, n−p prim, p ≤ n/2), plus komplette Minimalitäts-Neuberechnung nach Methode C.

**Läufe (Umgebung: Windows, Python 3.14.8, NumPy 2.4.3, Go 1.27.0, 12 Kerne)**

| Lauf | Ergebnis |
|---|---|
| C @ 200000 / 10^6 | reproduziert 383 / 523 (konsistent mit A/B) |
| C @ 10^7 | 4 999 999 gerade n, 0 Fehlschläge, max min-p = 751, 0,6 s |
| D @ 10^7 | identisch; Witness-Dateien C vs D **byte-identisch** (5 091 112 Bytes) |
| D @ 10^8 | 49 999 999 gerade n, 0 Fehlschläge, max min-p = 1093, 0,72 s |
| V @ 10^8 | alle Checks OK (Existenz + Minimalität, 17,7 s), SHA256 der Witness-Datei notiert |

**Analyse**

- Vier strukturell unabhängige Implementierungen (A: Liste, B: Hash-Set, C: NumPy-Restmengen, D: Go-Bitsieb) agreeieren; die Witness-Datei macht jeden Einzelfall prüfbar, ohne die Datei vertrauen zu müssen (Verifier rechnet sie neu).
- max min-p: 383 (2·10^5) → 523 (10^6) → 751 (10^7) → 1093 (10^8); wächst deutlich langsamer als n — konsistent mit der (unbewiesenen) Heuristik min-p ≪ n und mit OHP14 (9781 bei 4·10^18).
- Status unverändert: **endliche Verifikation, kein Beweis** von G_bin.

**Verworfene Alternativen (Warum)**

- C++/Rust statt Go: kein C-Compiler vorhanden; Rust vorhanden, aber Go reicht und ist einfacher auditierbar — keine Notwendigkeit.
- NumPy @ 10^8 als Primär-Lauf: machbar, aber Go ist 20× schneller und speichersparsamer; NumPy bleibt als unabhängiger Verifier im Einsatz.
- Spark/Cloud: 0-€-Budget; stattdessen GitHub Actions (public repo, kostenlos) — folgt als nächster Schritt.

**Nächster Schritt**

- Commit+Push; GitHub-Actions-Workflow für N=10^9 (kostenlose Runner); elementare Sätze 5–6; Doku-Update.

---

## 2026-10-01 — Meilenstein 10^9 (CI + vollständige Gegenverifikation), Sätze 5–7, Literatur/KI-Recherche (v4)

**Rechenläufe**

- Methode A/B zusätzlich bei 10^7: je 0 Fehlschläge, max min-p = 751 (7,7 s / 4,0 s) → **vier Methoden agreeieren** auf 10^7.
- **GitHub Actions (kostenlos, public repo):** Workflow `.github/workflows/goldbach.yml` (Build → Selbsttest N=2·10^5 mit erzwungenem 383-Ergebnis → Lauf N=10^9 → SHA256 → Artefakt → Auto-Commit). Run 36891298929: **success in 1 m 11 s**; Ergebnis: 499 999 999 gerade n ≤ 10^9, **0 Fehlschläge**, max min-p = **1789**, Go 1.27.1, 4 vCPU, 13,2 s Rechenzeit.
- Artefakt (524 383 817 Bytes) heruntergeladen; **SHA256 identisch** zur CI-Aufzeichnung (`db9b61ac…dbd8`).
- **Vollständige lokale Gegenverifikation** (`verify_witnesses2.py`, int32 + gechunkter vektorisierter Varint-Decoder): Header/CRC/Tokenzahl ✓, **jedes** Witness gültig (2 ≤ p ≤ n/2, p prim, n−p prim) ✓, **Minimalität komplett neu gerechnet** (Methode C) → **0 Abweichungen**, max min-p = 1789. Gesamt 112,7 s. Verifier vorher an der bereits geprüften 10^8-Datei validiert.

**Neue Beweise (elementar, lückenlos; `01_problemstellung/ELEMENTARE_SAETZE.md`)**

- **Satz 5 (Bertrand):** Erdős-Argument mit vollständig ausgeführtem Produktlemma \(P(n)<4^{n+2\lceil\log_2 n\rceil}\) (Beweis über die Rekursion \(P(2m)\le P(m)\binom{2m}{m}<4^mP(m)\) + \(\lceil n/2\rceil\)-Induktion), analytischer Bereich n ≥ 8192 mit expliziter G-Funktion und Ableitungsabschätzung, endlicher Bereich per zertifizierter Primzahlkette bis 10007 (jede Primheit per Probedivision + Maschinencheck). **Während des Schreibens korrigiert:** die naive Induktion \(P(n+1)=P(n)(n+1)\) scheitert am Primfall (Faktor q > 4); die Korrektur steht hier als dokumentierter Verwerfungsgrund.
- **Satz 6:** jede ganze Zahl n ≥ 2 ist Summe von höchstens \(\lfloor\log_2 n\rfloor+1\) Primzahlen (Induktion über Satz 5, konstruktiv).
- **Satz 7:** Korrektheit des Eratosthenes-Siebs (begründet formal den logischen Status aller Verifikationsläufe).
- Maschinenchecks (`test_goldbach.py`): Ketten-Primheit/Lücken, Bertrand numerisch bis 10^5, Satz-6-Zerlegungen bis 5000 → **ALLE TESTS OK**.

**Recherche (Hintergrundagent 2, abgeschlossen; Datei `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md`, 28 Quellen)**

- **KI/LLM:** AlphaProof/AlphaEvolve/LLM-Agenten/Taos ETP haben G_bin 2024–2026 **nicht angegangen** — kein Arbeitsersparnis-Potenzial; Erwartung bestätigt.
- **Formale Verifikation:** ternäre Goldbach existiert als Lean-4-Standalone-Projekt (Bialer, „computational trust boundary", KI-assisted) — methodisches Vorbild für unsere Witness-/Vertrauensgrenzen-Architektur; kein AFP/Coq/mathlib-Eintrag.
- **Rekorde:** akademischer Verifikationsrekord bleibt 4·10^18 (OHP14); darüber nur unrefereierte Claims (Gridbach-Medium-Post, GPU-Preprint arXiv:2603.07850).
- **Explizite Schranken:** bester Ausnahmemengen-Exponent Pintz 2018 (δ=0,28 ⇒ X^0,72); Zhao X^{7/10} und Schiavone X^{23/33} nur unrefereiert; Chen exp(exp(32,7)) v6 „to appear IJNT"; Vinogradov-Konstante obsolet.
- **Kostenlose Rechenleistung:** GitHub Actions für 10^9 geeignet (bestätigt durch unseren Lauf); primesieve geeigneter dritter Generator, aber ohne py3.14-Wheels (CLI-Weg offen); Colab/Kaggle nur für Heuristik.
- Hintergrundagent 1 (Literatur-Update `UPDATE_2026-10.md`) läuft noch; Einarbeitung folgt.

**Verworfene Alternativen (Warum)** — siehe auch `03_methoden/METHODENKATALOG.md`

- Naive Induktion im Produktlemma: mathematisch falsch (korrigiert, Grund dokumentiert).
- Full verify der 10^9-Datei mit Verifier v1 (int64): ~20 GB RAM-Bedarf > verfügbare 15,7 GB → v2 mit int32 + Streaming.
- Colab/Kaggle für Verifikation: Session-Limits/Verbote machen deterministische Läufe unbrauchbar.

**Nächster Schritt**

- Push v4; Agent-1-Ergebnis einarbeiten; optional primesieve-Triangulation. G_bin bleibt **offen**.

---

## 2026-10-01 — Abschluss der Recherche-Phase: Literatur-Update direkt erarbeitet (v5)

**Anlass.** Hintergrundagent 1 (Literatur-Update) ist nach >2 h ohne Ergebnis inaktiv gegangen (kein Completion-Event, keine Datei). Erkenntnis protokolliert: für eng umrissene Rechercheaufträge war der direkte Weg in dieser Umgebung zuverlässiger als der lange laufende Hintergrundagent (Agent 2 lief dagegen erfolgreich durch — der Unterschied war vermutlich der weitere, vage umrissene Auftrag von Agent 1).

**Recherche (durchgeführt von der Verwalter-Sitzung)**

- https://sweet.ua.pt/tos/goldbach.html **geöffnet**: Verifikation bis 4·10^18 (April 2012), **Double-Check bis 4·10^17** (581 701 Intervalle à 10^12), minimale-Partition-Methode, segmentiertes Sieb + Assembly, ~781,8 Single-CPU-Jahre, 48 min pro 10^12-Intervall nahe 10^18 (3,3-GHz-Kern).
- Helfgott-Buchstatus (Suchtreffer, Sekundär): *Annals of Mathematics Studies* Band 203 kursiert; physische Publikation nicht eindeutig bestätigt → arXiv-Fassungen bleiben kanonisch.
- Ramaré–Saouter: J. Number Theory 98 (2003), 10–33 (Suchtreffer, ScienceDirect + Autoren-PDF); Rolle: explizite kurze Primzahl-Intervalle; Baustein der 8,37·10²⁶-Schranke für ungerade Goldbach (laut OHP14-Abstract). Die im Suchtreffer kursierende Zahl „1,13·10²² ≈ e^28" wurde **bewusst nicht** als kanonisch übernommen (Kontext offensichtlich verkürzt; Blattlektüre offen).
- Behauptete Beweise 2024–2026 (Suchtreffer): **keiner** anerkannt; Wikipedia/Status unverändert; Amateuransätze (Reddit, Studentensymposium mit Bertrand-Ansatz); MathWorld: Pogorzelski 1977 „not generally accepted"; ein KI-Claim betrifft nur eine **Goldbach-artige** Liouville-Funktions-Vermutung — Verwechslungsmuster dokumentiert.

**Ergebnis**

- `02_literatur/UPDATE_2026-10.md` geschrieben (mit ehrlicher Kennzeichnung „geöffnet" vs. „Suchtreffer"), `QUELLEN.md`-Verweise aktualisiert.
- Damit sind ALLE Auftragspunkte der Recherche abgedeckt: Rekord (4·10^18, belegt), Helfgott-Status, Ramaré–Saouter, KI-/LLM-Stand (kein Ansatz auf G_bin), kostenlose Rechenleistung (GitHub Actions real genutzt), alte Schranken (Pintz δ=0,28 usw.).

**Verworfene Alternativen (Warum)**

- Neuen Hintergrundagenten für die Restrecherche starten: nach dem Ausfall zuverlässiger, direkt zu recherchieren (4 Web-Zugriffe); Agenten bleiben für parallelisierbare Blöcke nützlich, nicht für kurze sequenzielle Nachfragen.
- Die Zahl e^28-adjazent als Schranke zitieren: nicht verifiziert, Kontext im Suchtreffer verzerrt — bewusst weggelassen.

**Nächster Schritt**

- Commit+Push v5. Projektphase „Verifikation + Beweisteile + Recherche" ist abgeschlossen; Entscheidung über Weiterlauf (z. B. N > 10^9 via CI-Matrix, M–V-Blattlektüre) beim Nutzer. G_bin bleibt **offen** — kein Beweis, kein Scheinbeweis.

---

## 2026-10-01 — STOPP und Archivierung durch Nutzerentscheidung (v6, final)

**Entscheidung.** Nutzer hat das Projekt gestoppt („wir stoppen das … schau das mit den Stand und Verweise und warum und wieso das nicht ging und archivieren dann das repo"). Hintergrund: Ein Beweis von \(G_{\mathrm{bin}}\) war, wie von Anfang an ehrlich kommuniziert, nicht erreichbar (offenes Problem seit 1742; KI/LLM-Analyse bestätigte: kein Ansatzpunkt vorhanden).

**Letzte Fachaktion vor dem Stopp (vollendet und getestet, dann eingefroren)**

- Segmentmodus in `06_verifikation/go/goldbach_check.go` (`-A`-Start, Formate GBWIT1/GBWITSEG1) für künftige CI-Matrix-Läufe implementiert und **zweifach regressionsgetestet**: (1) A=4-Witness-Datei byte-identisch zum v4-Monolith-Lauf; (2) Segment-Payload [4000002, 10^7] identisch mit dem Tokenfenster des Voll-Laufs. Bewusst **nicht** als produktives Feature deklariert: Matrix-Workflow und Verifier-Unterstützung für GBWITSEG1 fehlen (dokumentiert in `06_verifikation/ANLEITUNG.md`).

**Abschlussdokumentation**

- Neu: `ABSCHLUSSBERICHT.md` — der eine zentrale Endstand-Report: (§2) Endstand mit Verweisen auf jede Datei, (§3) warum/wieso ein Beweis nicht möglich war (Minor-Arc-Lücke, „endlich ≠ alle n", KI-Stand, Fachstand), (§4) Betriebs-Log alles Nicht-Gegangenen mit Gründen, (§5) Wiederaufnahmebedingungen, (§6) Lizenz.
- `STATUS.md` und `README.md`: Archiv-Header mit Verweis auf den Abschlussbericht.
- `06_verifikation/ANLEITUNG.md`: Segmentmodus dokumentiert (inkl. Offen-Punkten).

**Archivierung**

- Finaler Commit+Push (v6), danach: Repo-Beschreibung aktualisiert und Repository auf GitHub **read-only archiviert**.
- Lokale Witness-Dateien (regenerierbar) bleiben auf dem Rechner des Nutzers.

**Schlussstatus (unverändert und endgültig protokolliert)**

- \(G_{\mathrm{bin}}\): **NICHT BEWIESEN** — offenes Problem. Kein Beweis, kein Scheinbeweis.
- Verifikation: alle geraden \(n\le10^9\), 0 Fehlschläge, max min-p = 1789, vollständig gegengeprüft.
- Bewiesen im Archiv: Sätze 1–7 (elementar, lückenlos, maschinengeprüft).
