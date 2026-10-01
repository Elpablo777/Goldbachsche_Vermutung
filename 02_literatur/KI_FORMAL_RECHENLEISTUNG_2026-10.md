# KI-/Formalisierungs- und Rechenleistungs-Update Oktober 2026

**Stand:** 2026-10-01. Rechercheblöcke: (1) formale Verifizierung/KI-Ära, (2) kostenlose Rechenleistung, (3) Wiederholungsprüfung alter expliziter Schranken.
**Zitierregel:** wie `QUELLEN.md` — nur URLs, die in dieser Sitzung per Suche („Suchtreffer") oder Fetch/Curl („geöffnet") getroffen wurden. „Folgt / folgt nicht" ist die Entscheidungs-Spalte für Gegenagenten. Nicht-Verifizierbares ist explizit markiert.

---

## 1. Formale Verifizierung / KI-Ära

### 1.1 Formalisierung der ternären Goldbach-Vermutung

1. Gershon Bialer: `ternary-goldbach-lean` (GitHub, Lean 4).  
   https://github.com/gersh/ternary-goldbach-lean (geöffnet 2026-10-01)  
   **Befund:** Lean-4-Formalisierung der ternären (schwachen) Goldbach-Vermutung, Theorem `ternary_goldbach : ∀ n : ℕ, Odd n → 7 ≤ n → IsThreePrimeSum n`. Stand laut README (2026-08-29): „complete" **unter einer expliziten, endlichen und computergestützten Vertrauensgrenze** („computational trust boundary"): Abhängigkeitskegel sorry-frei, keine `sorryAx`/`native_decide`-Atome; 104 registrierte Rechenläufe in 79 Kampagnen; einzelne Läufe bleiben **benannte Admissions-Axiome** („LeanCompCert"-Routen); externe Vertrauensatome u. a. Platt–Trudgian-RH-Verifikation und FLINT/Arb-Nullenumeration. „Full mode" (alle 9 Certificate-Stubs entladen) build-fertig am 2026-08-09 (~22.000 Build-Jobs). Autorenschaft: G. Bialer, Apache-2.0; **entwickelt interaktiv mit KI-Tools (Claude Code, Codex) unter seiner Leitung**; baut auf vendored Mathlib, `PrimeNumberTheoremAnd` (Kontorovich/Tao et al.) und LeanCert. Als finiter Teil wird die Helfgott–Platt-Verifikation bis \(8{,}875\cdot 10^{30}\) referenziert.  
   **Folgt:** Es existiert ein ernstzunehmendes, maschinengeprüftes Lean-4-Projekt zur ternären Goldbach-Vermutung — als **Standalone-Projekt mit deklarierter Vertrauensgrenze**, nicht als reines mathlib-Theorem. Methodisch interessant als Muster für „Zertifikat + explizite Vertrauensgrenze".  
   **Folgt nicht:** eine Formalisierung **innerhalb** von mathlib ohne externe Vertrauensaxiome; folgt nicht etwas für die **binäre** Vermutung (dort gibt es ohnehin nichts zu formalisieren — offen).

2. Archive of Formal Proofs (Isabelle/HOL, AFP) — **Negativbefund**.  
   https://www.isa-afp.org/topics/mathematics/number-theory/ (geöffnet 2026-10-01) + zwei Suchabfragen ohne Treffer  
   **Befund:** Die AFP-Zahlentheorie-Themenseite listet (Amicable_Numbers … Wieferich_Kempner) **keinen** Eintrag „Goldbach", „Helfgott" oder „Vinogradov"; auch eine gezielte Site-Suche blieb ohne Ergebnis.  
   **Folgt:** Zum Abrufzeitpunkt gibt es **keinen** AFP-Eintrag zur binären oder ternären Goldbach-Vermutung; Helfgotts Beweis ist in Isabelle/HOL **nicht** formalisiert.  
   **Folgt nicht:** dass eine In-House-Formalisierung unmöglich wäre; bitte vor Wiederverwendung der Negativaussage den Abrufzeitpunkt erneuern.

3. Coq/Rocq — **Negativbefund**.  
   Suchabfrage „Coq formalization Goldbach conjecture" (2026-10-01); verwertbarster Treffer: Proof Assistants Stack Exchange, https://proofassistants.stackexchange.com/questions/1161/ (nur Navigation)  
   **Folgt:** Kein Coq/Rocq-Formalisierungsprojekt der ternären Goldbach-Vermutung gefunden; die Diskussion bestätigt als Hindernis den massiven Computerteil des Beweises.  
   **Folgt nicht:** Nichtexistenz in allen Forks/Universitäten (nur: keine auffindbare, referenzierte Quelle).

4. Lean-Prover-Community, Zulip-Archiv „Checking the Goldbach conjecture".  
   https://leanprover-community.github.io/archive/stream/270676-lean4/topic/Checking.20the.20Goldbach.20conjecture.html (Suchtreffer)  
   **Folgt (als Diskussion, nicht als Theoremquelle):** Der Computerteil von Helfgotts Beweis (finites Verifikationsintervall in der Größenordnung \(10^{30}\)) ist die zentrale Hürde einer vollständigen Kern-Formalisierung — konsistent mit Quelle 1.  
   **Folgt nicht:** fertige Formalisierung.

### 1.2 KI-Systeme und die binäre Goldbach-Vermutung (Erwartung: NEIN — bestätigt)

5. Google DeepMind Blog: AlphaProof & AlphaGeometry 2, IMO 2024.  
   https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/ (geöffnet 2026-10-01)  
   **Befund:** Silbermedaillen-Niveau, 28/42 Punkte, 4 von 6 Wettbewerbsaufgaben; Methodik-Paper in *Nature* (2025-11-12). **Keine Erwähnung** der Goldbach-Vermutung oder anderer offener Forschungsprobleme.  
   **Folgt:** AlphaProof 2024 = Wettbewerbsmathematik (formalisierte IMO-Aufgaben).  
   **Folgt nicht:** irgendein Fortschritt an offenen Problemen wie \(G_{\mathrm{bin}}\).

6. Google DeepMind Blog: AlphaEvolve.  
   https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ (geöffnet 2026-10-01)  
   **Befund (2025-05-14):** Evolutionsbasierter Codier-Agent (Gemini Flash/Pro + Evaluator). Erfolge: 4×4-komplexe Matrixmultiplikation mit **48** Skalarmultiplikationen (Strassen 1969: 49); Kissing Number in Dimension 11: untere Schranke **593**; auf 50+ offenen Problemen in ~20 % der Fälle Verbesserung des besten bekannten Resultats. **Goldbach wird nicht erwähnt.**  
   **Folgt:** AlphaEvolve 2025 = algorithmische Verbesserungen/schärfere Konstruktionen an Einzelproblemen.  
   **Folgt nicht:** Fortschritt bei \(G_{\mathrm{bin}}\).

7. Tsoukalas et al. (Google-DeepMind-Umfeld): *Advancing Mathematics Research with AI-Driven Formal Proof Search*. arXiv:2605.22763.  
   https://arxiv.org/abs/2605.22763 (geöffnet 2026-10-01; v1 2026-05-21, v2 2026-06-08)  
   **Befund:** LLM-Agenten mit Lean-Verifikation lösen autonom **9 von 353 offenen Erdős-Problemen** (wenige hundert Dollar je Problem) und **44/492 OEIS-Vermutungen**. Goldbach wird auf der Abstract-Seite **nicht erwähnt**. (Presselabel „AlphaProof Nexus" geht auf Sekundärberichte zurück, z. B. the-decoder.com — Suchtreffer — und ist auf der arXiv-Seite so nicht belegt.)  
   **Folgt:** Der KI-Durchbruch 2025/26 bei offenen Problemen findet im „leichteren" Erdős/OEIS-Regime statt.  
   **Folgt nicht:** ein Ansatz von \(G_{\mathrm{bin}}\); auch nicht, dass die 9 gelösten Probleme zu Goldbach korrespondieren.

8. Terence Tao: Abschlussbericht des Equational Theories Project (ETP), 2025-12-09.  
   https://terrytao.wordpress.com/2025/12/09/the-equational-theories-project-advancing-collaborative-mathematical-research-at-scale/ (geöffnet 2026-10-01; Preprint arXiv:2512.07087, Suchtreffer)  
   **Befund:** Massen-Kollaboration (Start Sept. 2024) über 4.694 Gleichungsgesetze von Magmas; die Hauptlast trugen **klassische ATPs (Vampire, Mace4, Prover9)** und Brute-Force-Suche; laut Tao spielten moderne KI-Tools **„keine große Rolle"**. Goldbach: keine Erwähnung.  
   **Folgt:** Taos großes KI-Experiment 2024/25 war ein Kollaborations-/ATP-Experiment, kein Vorstoß auf \(G_{\mathrm{bin}}\).  
   **Folgt nicht:** dass KI generell bei additiver Zahlentheorie offener Probleme scheitern *muss* — nur: hier bis Ende 2025 nicht geschehen.

9. Sekundärdiskurs (Meinungspiece, nicht peer-reviewed): „AI Cannot Prove Goldbach's Conjecture".  
   https://pub.towardsai.net/ai-cannot-prove-goldbachs-conjecture-115bca355678 (Suchtreffer)  
   **Folgt (als Stimmungsbild):** Die These „aktuelle KI kann \(G_{\mathrm{bin}}\) nicht beweisen" wird auch in Sekundärquellen vertreten; virale Social-Media-Claims „KI löst Goldbach" fanden in **keiner** der oben geöffneten Primärquellen (5–8) eine Bestätigung.  
   **Folgt nicht:** ein Beweis der Unmöglichkeit; als Quelle nur zur Diskursdokumentation geeignet.

**Zwischenfazit Block 1.2:** Erwartung bestätigt. Kein belastbarer Hinweis 2024–10/2026, dass AlphaProof, AlphaEvolve, GPT-/Claude-/Gemini-Agenten oder Taos Experimente die binäre Goldbach-Vermutung gelöst oder wesentlich vorangebracht hätten. Für dieses Archiv: **kein Arbeitsersparnis**, keine neu zu übernehmenden KI-Resultate.

### 1.3 Computer-Verifikationen jenseits von \(4\cdot 10^{18}\)

10. Hiroaki Jay Nakata: Gridbach (Blogbericht).  
    https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d (via Reader geöffnet 2026-10-01; Projektseite https://gridbach.com geöffnet, Navigation)  
    **Befund:** Claim: Bestätigung bis \(4\cdot 10^{18} + 7\cdot 10^{13}\) (April 2025), „neuer Weltrekord"; Browser-/WASM-verteilter Rechenverbund („Gridbach"), Go-CLI `gridbach-core` (MIT) auf GitHub. Der Autor räumt selbst ein: **keine offizielle Anerkennung, kein Peer-Review, keine Garantie**; Anerkennung als Rekord sei unsicher.  
    **Folgt:** Ein nicht-peer-reviewter Einzelclaim knapp jenseits von \(4\cdot 10^{18}\) existiert (deckungsgleich mit `QUELLEN.md` Eintrag 11 — dort damit **durch eigene Lektüre untermauert**).  
    **Folgt nicht:** ein akzeptierter akademischer Rekord; unabhängige Replikation/Double-Check.

11. *Empirical Verification of Goldbach's Conjecture Beyond Four (×10¹⁸)*, Preprints.org 202503.0949.  
    https://www.preprints.org/manuscript/202503.0949 (Suchtreffer; direkter Fetch blockiert HTTP 403 — **Inhalt nicht verifiziert**)  
    **Folgt (laut Suchtreffer-Abstract):** behauptet Verifikation jenseits von \(4\cdot 10^{18}\).  
    **Folgt nicht:** irgendetwas — als nicht einsehbaren Preprint hier **bewusst nicht weiterverwenden**; nur als Karten-Eintrag für Gegenagenten.

12. Isaac Llorente-Saguer: *A Lock-Free, Fully GPU-Resident Architecture for the Verification of Goldbach's Conjecture*. arXiv:2603.07850.  
    https://arxiv.org/abs/2603.07850 (geöffnet 2026-10-01; v1 2026-03-08)  
    **Befund:** Vollständig GPU-residente Architektur (Segmentgenerierung auf der GPU, lock-freies Work-Stealing, 64-Bit-Pipeline mit Überlaufabsicherung **mathematisch sauber bis \(\approx 1{,}84\cdot 10^{19}\)**); demonstrierte Verifikation bis \(10^{13}\) (36,5 s auf 1× RTX 5090 bis \(10^{12}\); \(10^{13}\) in 133,5 s auf 4 GPUs); Code open-source; **Preprint, nicht als peer-reviewed ausgewiesen**.  
    **Folgt:** Aktualisiert `QUELLEN.md` Eintrag 12 mit Details; die Architektur beansprucht Korrektheit bis \(1{,}84\cdot 10^{19}\), zeigt aber nur bis \(10^{13}\) Ergebnisse.  
    **Folgt nicht:** ein neuer geprüfter Schranken-Rekord; Ersatz für Oliveira e Silva et al. ohne Replikation.

13. PrimeGrid — **Negativbefund**.  
    https://www.primegrid.com/ (geöffnet 2026-10-01)  
    **Befund:** Aktuelle Subprojekte (Proth, Sierpinski, Fermat, AP27, …) enthalten **kein** Goldbach-Verifikationsprojekt.  
    **Folgt:** PrimeGrid trägt aktuell nicht zu Goldbach-Verifikationen jenseits von \(4\cdot 10^{18}\) bei.  
    **Folgt nicht:** dass private/geplante Projekte ausgeschlossen sind.

**Zwischenfazit Block 1.3:** Der akademische Referenzwert bleibt \(4\cdot 10^{18}\) (Oliveira e Silva–Herzog–Pardi). Alles darüber ist Stand heute: ein nicht-refereierter Einzelclaim (10) und GPU-Preprints (12). Keine Änderung für `STATUS.md` nötig.

---

## 2. Kostenlose Rechenleistung (0-€-Budget)

### 2.1 GitHub Actions für PUBLIC Repos (Primärquelle: docs.github.com)

14. GitHub Docs: *Billing und Nutzung* (Actions).  
    https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration (geöffnet 2026-10-01)  
    **Folgt:** Nutzung von **Standard-GitHub-hosted Runnern in Public Repos ist kostenlos** („usage is free for standard GitHub-hosted runners in public repositories, and for self-hosted runners"). Billing bei wiederverwendbaren Workflows hängt am Caller.  
    **Folgt nicht:** Unbegrenztheit von Artefakt-Speicher für private Repos (für Public-Repos irrelevant).

15. GitHub Docs: *Actions limits*.  
    https://docs.github.com/en/actions/reference/limits (geöffnet 2026-10-01)  
    **Folgt (Zahlen):** Laufzeit **6 h/Job** (GitHub-hosted; self-hosted 5 Tage), **35 Tage/Workflow-Run**, **256 Matrix-Jobs/Run**, 50 Re-Runs, 20 gleichzeitige Jobs (Free-Plan), Workflow-Datei ≤ 500 KB, 100 Queues je Concurrency-Gruppe, Artefakt-/Cache-Speicher (Cache 10 GB/Repo; Speicherquotas betreffen Primär private Repos), API: GITHUB_TOKEN 1.000 Anfragen/h/Repo.  
    **Folgt nicht:** eine Garantie auf Dauerläufe via Job-Ketten über Tage — 6 h/Job ist die harte Schranke; Segmentierung über Matrix/Conkatenation ist der Weg.

16. GitHub Docs: *GitHub-hosted runners reference*.  
    https://docs.github.com/en/actions/reference/runners/github-hosted-runners (geöffnet 2026-10-01)  
    **Folgt:** `ubuntu-latest`: **4 vCPU, 16 GB RAM, 14 GB SSD** (x64); `windows-latest`: 4/16/14; `macos-latest`: 3 (M1)/7 GB/14 GB (arm64); standard Runner für **Public Repos „free and unlimited"**.  
    **Folgt nicht:** Persistenz zwischen Jobs (jeder Job startet frisch; Ergebnisse müssen als Artefakte/Witnesses gesichert werden). Artefakt-Retention (Standard 90 Tage) war auf diesen Seiten nicht nachlesbar — hier **nicht verifiziert**, ggf. in `06_verifikation/ANLEITUNG.md` als eigene Randnotiz prüfen.

### 2.2 Google Colab Free / Kaggle (kurz)

17. Google Colab FAQ.  
    https://research.google.com/colaboratory/faq.html (geöffnet 2026-10-01)  
    **Folgt:** Freie Notebooks laufen **maximal 12 h** je Session („at most 12 hours, depending on availability"); Idle-Timeouts; **verboten**: SSH/remote, „running distributed computing workers" (können jederzeit abgeschaltet werden); CPU-only-„standard runtime" ist die empfohlene Standardauswahl; genaue Limits werden von Google bewusst nicht publiziert.  
    **Folgt nicht:** reproduzierbare Langläufe — Colab ist für deterministische Verifikationsläufe ungeeignet.

18. Kaggle Notebooks Docs.  
    https://www.kaggle.com/docs/notebooks (Suchtreffer; direkter Fetch schlug fehl — **als Suchtreffer zitiert**)  
    **Folgt (laut Suchtreffern):** **12 h** maximale Sessiondauer für CPU- und GPU-Notebooks (9 h TPU); ~30 GPU-Stunden/Woche Quote; CPU-only fällt nicht unter die GPU-Quote.  
    **Folgt nicht:** Garantien; für 10⁹-Läufe ebenfalls ungeeignet (Session-Nichtpersistenz, zufällige Beendigung).

### 2.3 primesieve (C++/CLI + Python-Bindings)

19. kimwalisch/primesieve (GitHub).  
    https://github.com/kimwalisch/primesieve (geöffnet 2026-10-01)  
    **Folgt:** Segmentiertes Eratosthenes-Sieb **mit Wheel-Faktorisierung**, \(O(n\log\log n)\) Zeit, \(O(\sqrt n)\) Speicher, nutzt L1/L2-Cache-Größen, standardmäßig mehr-threadig, Primzahlen/Prim-Tuplets bis \(2^{64}\); CLI + C/C++-Bibliothek; **Lizenz BSD-2-Clause**; Windows-Installation u. a. `winget install primesieve`; offizielle/community-Bindings u. a. für Python. Leistungsklasse (Lesart des README): PrimePi-Zählungen über Intervalle der Breite \(10^{11}\) je Thread in ~17–32 s in den Stresstests — für unser \(10^{9}\)-Regime diametral überdimensioniert (positiv gemeint).  
    **Folgt:** primesieve ist als **dritter, unabhängiger Primzahlgenerator** (neben den bestehenden Go-/Python-/NumPy-Wegen in `06_verifikation/`) technisch und lizenzrechtlich geeignet.  
    **Folgt nicht:** Unabhängigkeit im Archiv-Sinne automatisch — die Nutzung muss als eigener Code-Pfad (CLI-Subprozess mit eigener Witness-Auswertung) dokumentiert werden.

20. PyPI-Paket `primesieve` (JSON-API).  
    https://pypi.org/pypi/primesieve/json und https://pypi.org/pypi/primesieve/2.3.4/json (geöffnet 2026-10-01)  
    **Folgt:** Neueste Version **2.3.4**, hochgeladen **2024-09-30**, Lizenz **MIT** (Bindings), `requires_python` nicht gesetzt; **die Version 2.3.4 enthält ausschließlich das sdist `primesieve-2.3.4.tar.gz` — keine Wheels** (ältere 2.1.0 hatte Wheels nur bis cp38). Für Python 3.14 auf Windows bedeutet `pip install primesieve`: **Selbstbau aus dem Quellpaket** (Cython + C++-Compiler, MSVC).  
    **Folgt nicht:** vorkompilierte cp314-Windows-Wheels — die gibt es (Stand 2026-10) **nicht**.

21. shlomif/primesieve-python (GitHub, Bindings).  
    https://github.com/shlomif/primesieve-python (geöffnet 2026-10-01)  
    **Folgt:** Cython-basierte Bindings, MIT, auch auf conda-forge als `python-primesieve`; README verspricht Wheels für Windows/macOS/Linux und „Python 3.5+", konkretisiert aber keine 3.13/3.14-Matrix — konsistent mit Quelle 20: für Python 3.14/Windows ist von einem Build-von-Quelle auszugehen.  
    **Folgt nicht:** dass der pip-Weg unter Python 3.14 ohne Compiler abläuft.

---

## 3. Wiederholungsprüfung alter Resultate (explizite Schranken 2020–2026)

22. G. Bhowmik, L. Grimmelt: *The exceptional set of the Goldbach problem*. arXiv:2607.27282.  
    https://arxiv.org/abs/2607.27282 und https://arxiv.org/html/2607.27282v2 (geöffnet 2026-10-01; v1 2026-07-29, v2 2026-08-13; laut Seite „to appear in *Analysis Mathematica*")  
    **Folgt (laut Paper):** Übersicht über Ausnahmemengen \(E(X)\) (Zahlen ≤ X, die nicht Summe von ≤ zwei Primzahlen sind) plus Neues: eine **voll explizite Major-Arcs-Formel** (glattes Major-Arc-Gewicht, alle Nullen sichtbar; Prop. 7.5 mit \(R=X^{\vartheta}\), \(0<\vartheta<4/9\)); außerdem: unter einer „sparse"-Version der Hardy–Littlewood-Vermutung keine „exceptional zeros". Historie laut Paper: Montgomery–Vaughan 1975 liefern \(E(X)\ll X^{1-\delta}\) mit **unbenanntem** (aber effektivem) \(\delta>0\); **Pintz 2018: explizit \(\delta=0{,}28\)**, d. h. \(E(X)\ll X^{0{,}72}\).  
    **Folgt:** Für `STATUS.md`-Arbeitsschritt 1 („\(\delta\) notieren"): Die kanonische M-V-Aussage bleibt „\(\delta>0\)"; der beste **explizite** Wert ist Pintz' 0,28 — nicht M-V selbst.  
    **Folgt nicht:** \(E(X)=0\) (selbstverständlich); und die Zitierung von 22 als Theoremquelle vor dem Erscheinen in *Analysis Mathematica*.

23. J. Pintz: *A new explicit formula in the additive theory of primes with applications II: The exceptional set in Goldbach's problem*. arXiv:1804.09084.  
    https://arxiv.org/abs/1804.09084 (Suchtreffer; über Quelle 22 mit \(\delta=0{,}28\) belegt)  
    **Folgt:** Primärquelle für \(E(X)\ll X^{0{,}72}\) (2018 — liegt knapp vor dem Suchfenster 2020–2026, wird aber erst durch die 2026er Übersicht als „beste explizite Schranke" sichtbar dokumentiert).  
    **Folgt nicht:** eine Verbesserung über 0,72 hinaus **in** Pintz.

24. G. Zhao: *The exceptional set of Goldbach problem and Linnik's constant*. arXiv:2511.05631.  
    https://arxiv.org/abs/2511.05631 (geöffnet 2026-10-01; v1 2025-11-07, v2 2026-01-23)  
    **Folgt (laut Abstract):** \(E(X)=O(X^{7/10})\) — **mit ineffektiver impliziter Konstante**; zusätzlich \(P(q)=O(q^{5})\) (kleinste Primzahl ≡ a mod q) aus derselben „Zero-Packet"-Methode.  
    **Folgt nicht:** eine effektive Konstante; und als Preprint nicht ohne Peer-Review als kanonische Schranke führen.

25. L. Schiavone: *A computer-assisted 23/33 + ε bound for the exceptional set in Goldbach's problem*.  
    https://lorenzoschiavone.com/writing/goldbach-exceptional-set-bound (geöffnet 2026-10-01; datiert 2026-07-18, **Selbstveröffentlichung ohne Peer-Review-Angabe**)  
    **Folgt (laut Paper):** \(E(X)\ll_{\varepsilon} X^{23/33+\varepsilon}\), Korollar \(E(X)\ll X^{0{,}69697}\); Verbesserung gegenüber Zhao (7/10) um exakt \(7/10-23/33=1/330\) und gegenüber Pintz (0,72); computer-assistiert mit rationalen Einhüllenden, Zeugendateien, SHA-256-Manifesten; baut auf Zhaos Zero-Packet-Rahmen und Pintz' Ausnahmemengen-Reduktion; Papier merkt selbst an: „does not prove the binary Goldbach conjecture"; Konstanten ineffektiv.  
    **Folgt nicht:** Referenzierbarkeit (nicht refereiert); kein Widerspruch zu \(G_{\mathrm{bin}}\) offen. **Behandlung wie Gridbach: dokumentieren, nicht kanonisieren.**

26. M. Bordignon, D. R. Johnston, V. Starichkova: *An explicit version of Chen's theorem and the linear sieve*. arXiv:2207.09452.  
    https://arxiv.org/abs/2207.09452 (geöffnet 2026-10-01; v6 2025-06-25, „To appear in Int. J. Number Theory")  
    **Folgt:** Bestätigt/aktualisiert `QUELLEN.md` Eintrag 16: jedes gerade \(N>\exp(\exp(32{,}7))\) ist \(p+P_2\); inzwischen journal-angemeldet (IJNT). Damit ist die explizite Chen-Schranke die **beste unbedingte** (Stand dieser Recherche).  
    **Folgt nicht:** \(p+p'\). (GRH-Variante: Bordignon–Starichkova, arXiv:2211.08844, Ramanujan J. 64 (2024), Schranke \(\exp(\exp(14))\) — nur Suchtreffer, nicht im Abstract dieser Sitzung geöffnet.)

27. D. Basak, R. N. Bhat, A. Dong, A. Zaharescu: *Almost all primes are not needed in Ternary Goldbach*. arXiv:2409.08968.  
    https://arxiv.org/abs/2409.08968 (geöffnet 2026-10-01; v1 2024-09-13)  
    **Folgt (laut Abstract):** Es gibt eine **dünn** (über admittierende Kongruenzsysteme definierte) Primteilmenge \(\mathbb{P}\), sodass die ternäre Goldbach-Aussage bereits mit Primzahlen aus \(\mathbb{P}\) gilt und fast alle Primzahlen nicht in \(\mathbb{P}\) liegen — qualitative Verschärfung von Helfgott.  
    **Folgt nicht:** numerisch explizite Konstanten (Abstract gibt keine); kein Einfluss auf \(G_{\mathrm{bin}}\).

28. Vinogradov-Konstante \(C\) — **Negativbefund**.  
    Suchabfragen zu „explicit Vinogradov constant ternary Goldbach improved 2021–2025" (2026-10-01)  
    **Folgt:** Es wurde **keine** 2020–2026-Arbeit gefunden, die eine „explizite Vinogradov-Konstante" verbessert — nach Helfgott (2013) ist \(C\) obsolet (jedes ungerade \(n\ge 7\)), und die explizite Literatur hat sich auf Chen-Schranken, Ausnahmemengen und Strukturfragen (26–27) verlagert. Historische GRH-Konstanten (z. B. Liu–Wang \(10^{20}\)) erscheinen nur als Suchkontext und werden hier **nicht** als Primärquelle geführt.  
    **Folgt nicht:** dass niemand je wieder \(C\)-artige Konstanten in schwächeren Settings angibt (z. B. nur mit „kleinen" Primzahlen).

---

## Konkrete Empfehlungen für dieses Archiv

- **Kein Umbruch, kein Arbeitsersparnis durch KI:** Alle Primärquellen (5–8) zeigen KI-Erfolge auf IMO-/Erdős-/OEIS-Niveau; \(G_{\mathrm{bin}}\) wurde von keinem System 2024–2026 angegangen. `STATUS.md` bleibt unverändert gültig („NICHT BEWIESEN"); `QUELLEN.md` Einträge 11/12 sind jetzt durch eigene Lektüre untermauert (Quellen 10/12) — ein Kurzupdate der `QUELLEN.md` durch den Archivverwalter wäre lohnend.
- **GitHub Actions eignet sich für einen \(10^{9}\)-Lauf:** 0 € in Public Repos (Quelle 14), ubuntu-latest mit 4 vCPU/16 GB/14 GB SSD (Quelle 16) reichen locker; das 6-h-Job-Limit (Quelle 15) ist gegen geschätzte Laufzeit eines Go-Segmentsiebs bis \(10^{9}\) (Größenordnung Minuten) irrelevant. Praktisch: Segmentierung per Matrix-Jobs (bis 256), Witness-Dateien je Segment als Artefakte hochladen; Ergebnisse liegen nach dem Job nicht mehr auf dem Runner vor. 20 parallele Jobs (Free) nicht überschreiten; Höflichkeits-Hinweis in `06_verifikation/ANLEITUNG.md` ergänzen.
- **primesieve als dritter unabhängiger Generator: ja, aber als CLI, nicht per pip.** BSD-2-Clause (Quelle 19), `winget install primesieve`; das Python-Binding hat Stand 2.3.4 (2024) **keine** Wheels (Quelle 20) und müsste unter Python 3.14/Windows aus dem Quellcode gebaut werden (MSVC + Cython). Für `06_verifikation/`: primesieve-CLI als eigenständiger Prozess, Ausgabe/Witnesses unabhängig gegen die Go- und Python-Pfade auswerten — saubere Triangulation.
- **Colab/Kaggle: nur für Heuristik, nie für Verifikation.** 12-h-Limit, Idle-Timeouts, verteilte Worker verboten (Quelle 17/18). Für `04_rechnungen/singular_series_stichprobe.txt`-artige NumPy-Experimente ok; für deterministische Checks ungeeignet.
- **Ausnahmemengen: Bester expliziter Stand dokumentieren.** M-V 1975: \(\delta>0\) ohne Wert; Pintz 2018: \(\delta=0{,}28\) → \(E(X)\ll X^{0{,}72}\) (Quellen 22/23); neu und noch nicht refereiert: Zhao \(X^{7/10}\) (ineffektiv, Quelle 24) und Schiavone \(X^{23/33}\) (computer-assistiert, Selbstverlag, Quelle 25). Für `05_beweisentwuerfe/` bzw. Literatur unter „beobachten, nicht kanonisieren" ablegen; für `STATUS.md`-Arbeitsschritt 1 gilt: das M-V-Original nennt keinen numerischen \(\delta\)-Wert — Pintz 0,28 ist die richtige Referenz für den besten expliziten Wert.
- **Chen-Schranke bestätigt und journalreif:** \(\exp(\exp(32{,}7))\) steht (v6/2025, IJNT angemeldet, Quelle 26); GRH-Variante \(\exp(\exp(14))\) (Ramanujan J. 2024) als Zusatz notieren. `QUELLEN.md` Eintrag 16 braucht nur eine Statuszeile „to appear IJNT".
- **Vinogradov-Konstante: kein Recherchebedarf mehr.** Nach Helfgott ist \(C\) obsolet (Quelle 28); keine 2020–2026-Verbesserung gefunden — im Archiv nichts nachziehen.
- **Methodische Inspiration aus der Lean-Welt:** Das Lean-4-Projekt (Quelle 1) modelliert genau das, was `06_verifikation/` mit `verify_witnesses.py` anstrebt: endliche Rechenläufe als benannte, überprüfbare Zertifikate mit **explizit deklarierter Vertrauensgrenze**. Beim nächsten Verifikationslauf die Vertrauensgrenze (welcher Generator, welche Hashes, welche Umgebungsannahmen) wie dort explizit auflisten.
