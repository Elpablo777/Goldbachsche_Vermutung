# STATUS — binäre Goldbachsche Vermutung

**Stand:** 2026-10-01  
**Projektstatus: ARCHIVIERT** (Nutzerentscheidung; Repository read-only). Endstand, Verweise und die vollständige Begründung, warum kein Beweis möglich war: **`ABSCHLUSSBERICHT.md`** — immer zuerst lesen.  
**Gesamtstatus der Zielaussage:** **NICHT BEWIESEN**

Die binäre (starke) Goldbach-Aussage

> Jede gerade ganze Zahl \(n \ge 4\) ist Summe zweier Primzahlen.

ist in diesem Archiv **kein Theorem**. Es liegt **kein lückenloser Beweis** vor, und es wird **kein Scheinbeweis** als Lösung ausgegeben.

## Was fest bewiesen ist (Literatur, nicht dieses Repo)

| Aussage | Status | Quelle (siehe `02_literatur/QUELLEN.md` + Update-Dateien) |
|---|---|---|
| Ternäre Goldbach: jedes ungerade \(n \ge 7\) ist Summe dreier Primzahlen | als bewiesen akzeptiert (Helfgott 2013 ff.) | arXiv:1312.7748, arXiv:1501.05438 |
| Vinogradov: jedes hinreichend große ungerade \(n\) ist Summe dreier Primzahlen | Theorem (1937) | Vinogradov |
| Chen: jedes hinreichend große gerade \(n\) ist \(p + P_2\) | Theorem (1966/1973); explizit \(N>\exp(\exp(32.7))\), v6/2025 „to appear IJNT" | Bordignon–Johnston–Starichkova arXiv:2207.09452 |
| Fast alle geraden \(n\) sind \(p+p'\) | Theorem; bester **expliziter** Ausnahmemengen-Exponent: Pintz 2018, \(\delta=0{,}28\) ⇒ \(E(X)\ll X^{0{,}72}\); neuer (unrefereiert): Zhao \(X^{7/10}\), Schiavone \(X^{23/33}\) | Estermann 1938; M–V 1975; Pintz arXiv:1804.09084; Details in `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md` |
| Binäre Goldbach für alle geraden \(n \le 4\cdot 10^{18}\) | empirisch/computergeprüft (akademischer Referenzwert), kein Beweis für alle \(n\) | Oliveira e Silva–Herzog–Pardi, Math. Comp. 83 (2014) |

**KI/LLM-Stand (geprüft 2026-10-01):** kein KI-System (AlphaProof, AlphaEvolve, LLM-Agenten, Taos ETP) hat \(G_{\mathrm{bin}}\) 2024–2026 angegangen oder vorangebracht; ternäre Goldbach existiert als Lean-4-Standalone-Formalisierung mit deklarierter „computational trust boundary". Details: `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md`.

## Was in diesem Workspace vollständig bewiesen ist (elementar)

- Sätze 1–4 in `01_problemstellung/ELEMENTARE_SAETZE.md`.
- **Satz 5 (Bertrandsches Postulat)** — Erdős-Beweis mit vollständig ausgeführtem Produktlemma \(P(n)<4^{\,n+2\lceil\log_2 n\rceil}\), Schwelle \(n\ge8192\), endlicher Rest per zertifizierter Primzahlkette bis 10007.
- **Satz 6** — jede ganze Zahl \(n\ge2\) ist Summe von höchstens \(\lfloor\log_2 n\rfloor+1\) Primzahlen (konstruktiv, Induktion über Satz 5).
- **Satz 7** — Korrektheit des Eratosthenes-Siebs (begründet die Verifikationsläufe formal).
- Alle drei maschinengeprüft in `06_verifikation/test_goldbach.py` (Kette, Bertrand bis \(10^5\), Satz-6-Zerlegungen bis \(5000\)): **ALLE TESTS OK** (2026-10-01).

## Was in diesem Workspace geprüft ist (Stand 2026-10-01)

**Vier strukturell unabhängige Methoden** (A: Sieb-Liste, B: Hash-Set, C: NumPy-Restmengen-Elimination, D: Go-Bitsieb, parallel):

| Intervall | Methoden | Ergebnis |
|---|---|---|
| \(4\le n\le 2\cdot10^5\) | A, B, C, D | je 99999 gerade n, 0 Fehlschläge, max min-\(p=383\) |
| \(4\le n\le 10^6\) | A, C, D | 499999 gerade n, 0 Fehlschläge, max min-\(p=523\) |
| \(4\le n\le 10^7\) | A, B, C, D | 4999999 gerade n, 0 Fehlschläge, max min-\(p=751\); Witness-Dateien C↔D **byte-identisch** |
| \(4\le n\le 10^8\) | D (lokal) + V (vollständige Gegenverifikation) | 49999999 gerade n, 0 Fehlschläge, max min-\(p=1093\); alle Witness gültig **und** minimal |
| \(4\le n\le 10^9\) | D (GitHub Actions, ubuntu-latest) + V2 (vollständige lokale Gegenverifikation) | **499999999 gerade n, 0 Fehlschläge, max min-\(p=1789\)**; SHA256 `db9b61ac…dbd8`, CRC ok, alle Witness gültig und minimal |

Vertrauensgrenze der Läufe (explizit, nach Lean-Vorbild): primärer Generator Methode D (Go 1.27, Bitsieb), Gegenrechner Methode C (NumPy), Umgebung + Hashes protokolliert in `06_verifikation/ANLEITUNG.md` und den Ergebnisdateien.

Diese Checks **ersetzen keinen Beweis**.

## Offene Lücke (der eigentliche Blocker) — unverändert

Für die binäre Form liefert die Kreismethode auf den Minor Arcs **keine** hinreichend starke Abschätzung, um \(r_2(n) > 0\) für alle großen geraden \(n\) zu erzwingen. Siebmethoden erreichen \(p+P_2\), nicht durchgängig \(p+p'\). Kein hier dokumentierter Weg schließt diese Lücke. Siehe `05_beweisentwuerfe/LUECKENANALYSE.md`.

## Nächster Arbeitsschritt

1. Montgomery–Vaughan-Original (*Acta Arith.* 27) gegenlesen — laut `KI_FORMAL_RECHENLEISTUNG_2026-10.md` (Quelle 22) nennt das Original selbst **keinen** numerischen \(\delta\)-Wert; bester expliziter Wert ist Pintz' \(\delta=0{,}28\) (2018). Blattlektüre bestätigt das.
2. Optional: primesieve (BSD-2-Clause) als dritter unabhängiger Primzahlgenerator per CLI (`winget install primesieve`), Ausgabe als eigener Code-Pfad gegen C/D triangulieren.
3. Kein Vorstoß als „Beweis von \(G_{\mathrm{bin}}\)“, solange Minor Arcs bzw. \(P_2\to P_1\) offen sind.
4. Gegenprüfung: `python 06_verifikation/test_goldbach.py` plus die Läufe in `06_verifikation/ANLEITUNG.md`.

## Leseordnung für Gegenprüfung

1. Dieses File  
2. `README.md`  
3. `00_laborjournal/JOURNAL.md`  
4. `01_problemstellung/ELEMENTARE_SAETZE.md` (Sätze 1–7)  
5. `07_publikationsentwurf/manuskript.md`  
6. Verifikation reproduzieren: Kommandos in `06_verifikation/ANLEITUNG.md` (2-Minuten-Check: `python 06_verifikation/goldbach_check_np.py 200000` → max min-p 383)
