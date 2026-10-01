# Methodeninventar

Legende: **W** = in diesem Archiv weiterverfolgt (Dokumentation/Rechnung).  
**L** = Literatur-Theorem, hier nur zitiert.  
**V** = verworfen als Weg zu einem vollständigen Beweis von \(G_{\mathrm{bin}}\) (mit Grund).  
**H** = Heuristik, keine Beweiskraft.

## 1. Elementare Zerlegung und kleine Fälle — W

Für \(n=4=2+2\). Für gerade \(n\ge 6\) sind beide Summanden ungerade, sobald man \(2+(n-2)\) nur nutzt falls \(n-2\) prim (Sophie-Germain-artig zufällig, nicht immer).  
Elementar prüfbar: endliche Listen. **Reicht nicht** für alle \(n\).

## 2. Sieb des Eratosthenes + Exhaustion — W (endlich)

Genau das Skript in `06_verifikation/`.  
**Beweisumfang:** nur \(n\le N\). Komplexität grob \(O(N\log\log N)\) plus \(O((N/\log N)\cdot \bar p)\) für die Suche; in der Praxis für \(N=2\cdot 10^5\) unter einer Sekunde.

**V für Unendlich:** kein Induktionsschritt von \(N\) auf \(N+2\).

## 3. Hardy–Littlewood-Kreismethode (binär) — H / V als Vollbeweis

Schreibe
\[
r_2(n)=\int_0^1 S(\alpha)^2 e^{-2\pi i n\alpha}\,d\alpha,\qquad S(\alpha)=\sum_{p\le n}\log p\; e^{2\pi i p\alpha}
\]
(oder Varianten ohne \(\log\)). Zerlegung in Major Arcs \(\mathfrak{M}\) (nahe \(a/q\) mit kleinem \(q\)) und Minor Arcs \(\mathfrak{m}\).

- Major Arcs: liefern den Hauptterm \(\mathfrak{S}(n) n\) (bzw. \(n/(\log n)^2\) je nach Gewichtung) — **bedingt kontrollierbar**.
- Minor Arcs: man braucht \(\sup_{\alpha\in\mathfrak{m}}|S(\alpha)|\) klein genug. Im **ternären** Problem steht \(S^3\), der Extrafaktor \(S\) rettet die Minor Arcs (Vinogradov/Helfgott). Im **binären** Problem fehlt dieser Faktor.

**Grund der Verwerfung als Vollbeweis:** die bekannten Minor-Arc-Schranken sind für \(S^2\) zu schwach, um \(r_2(n)>0\) für alle großen geraden \(n\) zu zeigen. Unter GRH werden die Major Arcs länger/besser, aber GRH ist selbst unbewiesen und selbst dann bleiben technische Lücken für ein vollständiges \(G_{\mathrm{bin}}\).

## 4. Vinogradov-Methode (ternär) — L

Exponentialsummen über Primzahlen, Typ-I/II-Summen. Löst das **Drei-Primzahlen-Problem** für große ungerade \(n\).  
**Nicht gewählt für \(G_{\mathrm{bin}}\):** falsche Parität der Anzahl der Summanden.

## 5. Helfgott (explizite Kreismethode, ternär) — L

Verbesserte Major- und Minor-Arc-Abschätzungen plus finite checks.  
**Nicht gewählt als binärer Beweis:** Autor und Fachgemeinschaft trennen die Probleme.

## 6. Lineares Sieb / Chen — L

Untersucht die Menge \(\{N-p: p\le N, p\in\mathbb{P}\}\) auf fastprime Faktoren. Chen erreicht \(P_2\).  
**V als Goldbach-Beweis:** der Term, der dreifache Fastprime abzieht, lässt sich nicht auf 0 für den \(P_1\)-Anteil drücken.

## 7. Goldston–Pintz–Yıldırım / Zhang / Maynard (beschränkte Lücken) — V

Infinit viele Primzahllücken \(\le H\).  
**Folgt nicht:** für festes gerades \(N\) existiert \(p\) mit \(N-p\) prim. Lückenresultate sind Verschiebungen in der *Primzahlzeile*, nicht in der *additiven Gleichung* \(p+q=N\).

## 8. RH / GRH als Hypothese — H (bedingt)

Hardy–Littlewood und spätere Arbeiten: unter GRH gilt Goldbach für große \(n\) in abgeschwächten oder fast-allen-Formen (je nach Satz).  
**V als unbedingte Lösung:** die Hypothese ist offener als viele Teilresultate.

## 9. „Jedes gerade n ist 2p oder hat kleine Primteiler von n-p“ naive Diversität — V

Klingt nach Dirichlet, liefert aber keine gleichmäßige untere Schranke für \(\pi(n; n, b)\) im benötigten Bereich \(b=n-p\) mit \(p\) prim.

## Gewählte Linie dieses Archivs

1. Aussage trennen (\(G_{\mathrm{bin}}\) vs. \(G_{\mathrm{ter}}\) vs. Chen).  
2. Endliche Checks reproduzierbar machen.  
3. Die Minor-Arc-Lücke als präzisen Blocker festhalten.  
4. Keinen neuen analytischen Durchbruch vortäuschen.

## Ergänzt 2026-10-01: Verifikationsarchitektur (Methoden C/D, CI, Verifier)

- **Methode C (NumPy, vektorisiert) — W:** Restmengen-Elimination über \(k=n/2\); minimales \(p\) durch aufsteigende Primzahl-Pässe. „Dead"-\(k\) sind nach explizitem Argument endgültige Fehlschläge. 10^7 in 0,6 s.
- **Methode D (Go, ungerades Bitsieb, parallel) — W:** vollständig unabhängige Sprache/Implementierung; schreibt Witness-Dateien (GBWIT1: LEB128 + CRC32). 10^8 lokal in 0,72 s; **10^9 auf GitHub Actions** in 13,2 s Rechenzeit.
- **Witness-Datei + unabhängiger Verifier — W (Vertrauensarchitektur):** der Generator muss nicht vertraut werden; der Verifier (Python/NumPy, int32 + gechunkter Varint-Decoder) liest die Datei, prüft CRC, **jedes** Witness (Gültigkeit) und rechnet die **Minimalität** komplett neu (Methode C). Validiert an 10^8, angewandt auf die 10^9-CI-Datei: 0 Abweichungen. Muster: „endliche Rechenläufe als benannte, überprüfbare Zertifikate mit expliziter Vertrauensgrenze" — methodisch inspiriert vom Lean-4-Projekt zur ternären Goldbach-Vermutung (siehe `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md`, Quelle 1).
- **GitHub Actions als kostenlose Rechenleistung — W:** public repo = 0 €; ubuntu-latest (4 vCPU, 16 GB RAM) reicht für 10^9 deutlich (6-h-Job-Limit irrelevant); Witness als Artefakt (90 Tage), Ergebnisdatei auto-committet. Limits recherchiert: ebenda, Quellen 14–16.
- **Verworfene/nicht gewählte Alternativen (mit Grund):**
  - *C++/Rust statt Go:* kein C-Compiler vorhanden; Rust vorhanden, aber Go einfacher auditierbar — kein Mehrwert.
  - *NumPy als 10^9-Primärgenerator:* machbar, aber ~10× langsamer und speicherhungriger; NumPy bleibt Verifier (stärkere Rolle: unabhängige Gegenrechnung).
  - *primesieve als dritter Primzahlgenerator:* umgesetzt (2026-10-01, `winget install primesieve`, v12.16, BSD-2-Clause): π(10⁹) = 50 847 534 und die Primzahl-Liste in [999·10⁶, 10⁹] stimmen exakt mit dem NumPy-Sieb überein (`06_verifikation/triangulierung_primesieve.txt`) — empirische Triangulation der Sieb-Korrektheit über Satz 7 hinaus.
  - *Google Colab/Kaggle für Verifikationsläufe:* 12-h-Session-Limits, Idle-Timeouts, verteilte Worker verboten — nur für Heuristik-Experimente geeignet, nie für deterministische Checks.
  - *Gridbach-/GPU-Preprint-Schranken über 4·10^18 als Referenz:* nicht refereiert — dokumentiert (Quellen 10/12 in `KI_FORMAL_RECHENLEISTUNG_2026-10.md`), nicht kanonisiert.
  - *Neue analytischen Anläufe (Minor Arcs selbst angreifen):* außer Reichweite dieser Sitzung; die Lücke ist präzise in `05_beweisentwuerfe/LUECKENANALYSE.md` dokumentiert statt mit Pseudo-Fortschritt gefüllt.
