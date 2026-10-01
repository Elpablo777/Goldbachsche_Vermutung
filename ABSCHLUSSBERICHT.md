# Abschlussbericht — Forschungsarchiv zur binären Goldbachschen Vermutung

**Datum:** 2026-10-01  
**Status: ARCHIVIERT (auf Nutzerentscheidung; Repo read-only)**  
**Status der Zielaussage \(G_{\mathrm{bin}}\): NICHT BEWIESEN — offenes Problem seit 1742**

---

## 1. Ergebnis in einem Satz

Ein Beweis der binären Goldbachschen Vermutung war **nicht** erreichbar — weder durch Rechnung, noch durch Recherche, noch durch KI-Systeme; stattdessen liegt ein vollständig dokumentiertes, reproduzierbares Forschungsarchiv mit massiv erweiterter endlicher Verifikation (bis \(10^9\)), drei neu bewiesenen elementaren Sätzen und einer 32+ Quellen umfassenden Literatur-/KI-Analyse vor, alles auf GitHub archiviert und von jedem Gegenprüfungs-Agenten auditierbar.

## 2. Endstand mit Verweisen

| Liefergegenstand | Ergebnis | Datei/Verweis |
|---|---|---|
| Verifikation \(4\le n\le10^9\) | 499 999 999 gerade n, **0 Fehlschläge**, max min-p = 1789 | `06_verifikation/ergebnis_go_N1000000000.txt`, `verify2_report_N1000000000.txt` |
| Vier unabhängige Methoden A/B/C/D | agreeieren auf 10^7 (0 Fehler, max min-p 751); C↔D-Witness-Dateien **byte-identisch** | `06_verifikation/ANLEITUNG.md` (Tabelle aller Läufe) |
| 10^9-Lauf auf kostenloser Rechenleistung | GitHub Actions, 0 €, 13,2 s Rechenzeit, Witness 524 MB als Artefakt | `.github/workflows/goldbach.yml`, `sha256_N1000000000.txt` |
| Vollständige Gegenverifikation | jedes Witness gültig (p prim, n−p prim) **und minimal**, 0 Abweichungen | `06_verifikation/verify_witnesses2.py` |
| Dritter Primzahlgenerator (Triangulation) | primesieve 12.16: π(10⁹) und Segment-Primzahlen identisch zum NumPy-Sieb | `06_verifikation/triangulierung_primesieve.txt` |
| **Bewiesene elementare Sätze** | Satz 5 (Bertrand, Erdős-Beweis mit Produktlemma), Satz 6 (O(log n)-Primzahlzerlegung), Satz 7 (Siebkorrektheit); Maschinenchecks: ALLE TESTS OK | `01_problemstellung/ELEMENTARE_SAETZE.md`, `06_verifikation/test_goldbach.py` |
| KI-/LLM-Analyse | AlphaProof, AlphaEvolve, LLM-Agenten, Taos ETP haben \(G_{\mathrm{bin}}\) **nie angegangen** — kein Arbeitsersparnis-Potenzial | `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md` (Block 1.2) |
| Literatur-Stand | Rekord unverändert 4·10^18 (Double-Check bis 4·10^17, ~781,8 CPU-Jahre); Pintz δ=0,28 bester expliziter Ausnahmemengen-Exponent; Chen exp(exp(32,7)) „to appear IJNT“; behauptete Beweise 2024–2026: **keiner** anerkannt | `02_literatur/UPDATE_2026-10.md`, `02_literatur/QUELLEN.md` |
| Methodeninventar inkl. Verwerfungen | jeder nicht gewählte Weg mit Grund | `03_methoden/METHODENKATALOG.md` |
| Lückenanalyse (Blocker) | Minor-Arc-Lücke / P₂→P₁ präzise dokumentiert | `05_beweisentwuerfe/LUECKENANALYSE.md` |
| Publikationsentwurf | Preprint-Stil, alle Ergebnisse referenziert | `07_publikationsentwurf/manuskript.md` |
| Zeitspur | 5 Journaleinträge, 6 Patchlog-Einträge | `00_laborjournal/JOURNAL.md`, `PATCHLOG.md` |
| Segmentmodus (für Wiederaufnahme) | Go-Programm mit `-A`-Start; **getestet**: A=4-Witness byte-identisch zum Voll-Lauf, Segment-Payload = Tokenfenster des Voll-Laufs | `06_verifikation/go/goldbach_check.go` |

## 3. Warum und wieso es (mathematisch) nicht ging

1. **Der harte Kern:** Für die Kreismethode fehlt auf den Minor Arcs eine Abschätzung, die \(r_2(n)>0\) für **alle** großen geraden \(n\) erzwingt; die ternäre Form hat den rettenden Extrafaktor \(S(\alpha)^3\), die binäre (\(S(\alpha)^2\)) nicht. Siebmethoden stoppen bei \(p+P_2\) (Chen); der Übergang \(P_2\to P_1\) ist genau das ungelöste Restproblem. Vollständig ausgeführt: `05_beweisentwuerfe/LUECKENANALYSE.md`.
2. **Rechnung kann es nicht ersetzen:** Endliche Verifikation bis \(N\) hat keinen Induktionsschritt auf \(N+2\) — selbst \(N=10^{100}\) wäre kein Beweis. Die Vermutung ist seit 1742 offen; die Fachgemeinschaft hat alle hier dokumentierten Wege (Kreismethode, Siebe, transference, bounded gaps, GRH-bedingte Aussagen) geprüft — Inventar mit Verwerfungsgründen in `03_methoden/METHODENKATALOG.md`.
3. **KI/LLM-Era-Recherche:** Der Auftrag lautete, zu prüfen, ob moderne KI Arbeit ersparen kann. Ergebnis (32 Quellen, primärgeprüft): **nein** — AlphaProof (IMO-Niveau), AlphaEvolve (Algorithmik), LLM-Agenten (Erdős-/OEIS-Regime) und Taos ETP („AI did not play a major role“) berühren \(G_{\mathrm{bin}}\) nicht; die ternäre Vermutung existiert nur als Lean-4-Standalone-Formalisierung mit deklarierter „computational trust boundary“ (methodisches Vorbild für unsere Witness-Architektur). Siehe `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md`.
4. **Fachstand als Obergrenze des Machbaren:** Akademischer Verifikationsrekord 4·10^18 (Double-Check bis 4·10^17); über dem nur unrefereierte Einzelclaims. Bestes bewiesenes Fast-alle-Resultat \(E(X)\ll X^{0{,}72}\) (Pintz 2018) lässt theoretisch unendlich viele Ausnahmen zu — „fast alle“ ist nicht „alle“.
5. **Ehrlichkeitsregel des Archivs:** Ein erfundener oder lückenhafter „Beweis“ wäre wissenschaftlich wertlos und wurde von Anfang an ausgeschlossen (`README.md`, `01_problemstellung/FORMULIERUNG.md`). Deshalb: kein QED ohne geschlossene Quantorenschichten.

## 4. Was im Projektverlauf konkret nicht ging (Betriebs-Log)

| Vorfall/Fehler | Was passiert ist | Umgang/Grund |
|---|---|---|
| Hintergrundagent „Literatur-Update“ | lief >2 h, ging ergebnislos inaktiv (keine Datei, kein Completion-Event) | Restauftrag direkt erledigt (4 Web-Zugriffe) → `02_literatur/UPDATE_2026-10.md`; Erkenntnis: kurze, scharf umrissene Aufträge direkt, breite Blöcke als Agent |
| Fehler im Produktlemma von Satz 5 | naive Induktion \(P(n+1)=P(n)\cdot(n+1)\) scheitert im Primfall (Faktor \(q>4\)) | korrigiert über Rekursion \(P(2m)\le P(m)\binom{2m}{m}<4^mP(m)\); Verwerfungsgrund im Journal (v4) |
| Verifier v1 für 10^9 | int64-Allokation ≈ 20 GB > 15,7 GB freier RAM | Verifier v2 (int32 + gechunkter Varint-Decoder), vorher an 10^8 validiert |
| Colab/Kaggle für Verifikationsläufe | 12-h-Session-Limits, Idle-Timeouts, verteilte Worker verboten | verworfen; GitHub Actions stattdessen real genutzt |
| C++/Rust statt Go | kein C-Compiler; Rust vorhanden, aber Go einfacher auditierbar | verworfen, kein Mehrwert |
| CI-Artefakt fast zu groß | 524-MB-Witness in Unterordner durch `.gitignore`-Muster nicht erfasst → Push-Abstoßung (GitHub-100-MB-Limit) | `.gitignore`-Muster erweitert, Commit amendiert; Datei bleibt lokal/regenerierbar |
| Push mit privater Mailadresse | GitHub-E-Mail-Privatsphäre blockierte den ersten Push | Repo-lokal NoReply-Adresse gesetzt (JOURNAL v2) |
| KI-Claim „GPT-6 Astra beweist Goldbach“ | betrifft laut Quelle nur eine **Goldbach-artige** Liouville-Funktions-Vermutung | als Verwechslungsmuster dokumentiert (`UPDATE_2026-10.md` §4) |

## 5. Bedingung für eine Wiederaufnahme

- **Beweis-Chance:** nur bei einem neuen Fachdurchbruch (Minor-Arc-Abschätzung bzw. \(P_2\to P_1\)) — dann ist das Archiv die fertige Ausgangsbasis (Formulierung, Literatur, Lückenanalyse).
- **Rechen-Ausbau:** der getestete Segmentmodus (`go/goldbach_check.go -A … -N …`) ist die Vorarbeit für CI-Matrix-Läufe (10 × 10^9-Segmente → 10^10). **Offen:** Matrix-Workflow und GBWITSEG1-Unterstützung im Verifier waren bei Archivierung noch nicht umgesetzt — das ist dokumentiert, nicht halbfertig als „fertig“ deklariert.
- **Gegenprüfung jederzeit:** Kommandos in `06_verifikation/ANLEITUNG.md` (2-Minuten-Check) und `README.md`.

## 6. Lizenz und Persistenz

CC BY-NC-SA 4.0. Das Repository https://github.com/Elpablo777/Goldbachsche_Vermutung ist auf read-only archiviert; lokale Witness-Dateien (regenerierbar) verbleiben auf dem Rechner des Nutzers.
