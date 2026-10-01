# STATUS — binäre Goldbachsche Vermutung

**Stand:** 2026-09-29  
**Gesamtstatus der Zielaussage:** **NICHT BEWIESEN**

Die binäre (starke) Goldbach-Aussage

> Jede gerade ganze Zahl \(n \ge 4\) ist Summe zweier Primzahlen.

ist in diesem Archiv **kein Theorem**. Es liegt **kein lückenloser Beweis** vor, und es wird **kein Scheinbeweis** als Lösung ausgegeben.

## Was fest bewiesen ist (Literatur, nicht dieses Repo)

| Aussage | Status | Quelle (siehe `02_literatur/QUELLEN.md`) |
|---|---|---|
| Ternäre Goldbach: jedes ungerade \(n \ge 7\) ist Summe dreier Primzahlen | in der Fachgemeinschaft als bewiesen akzeptiert (Helfgott 2013 ff.) | arXiv:1312.7748, arXiv:1501.05438 |
| Vinogradov: jedes hinreichend große ungerade \(n\) ist Summe dreier Primzahlen | Theorem (1937) | Vinogradov |
| Chen: jedes hinreichend große gerade \(n\) ist \(p + P_2\) | Theorem (1966/1973); explizit z. B. \(N>\exp(\exp(32.7))\) | Chen; Bordignon–Johnston–Starichkova arXiv:2207.09452 |
| Fast alle geraden \(n\) sind \(p+p'\) | Theorem (Estermann u. a.; Montgomery–Vaughan \(E(X)\ll X^{1-\delta}\)) | Estermann 1938; Montgomery–Vaughan 1975 |
| Binäre Goldbach für alle geraden \(n \le 4\cdot 10^{18}\) | empirisch/computergeprüft, kein Beweis für alle \(n\) | Oliveira e Silva–Herzog–Pardi, Math. Comp. 83 (2014) |

## Was in diesem Workspace vollständig bewiesen ist (elementar)

- Sätze 1–4 in `01_problemstellung/ELEMENTARE_SAETZE.md` (u. a. \(4=2+2\); \(G_{\mathrm{bin}}\Rightarrow G_{\mathrm{ter}}\); explizite Partitionen bis \(30\)).

## Was in diesem Workspace geprüft ist

- Methode A: `06_verifikation/ergebnis_N200000.txt` — 99999 gerade \(n\le 200000\), 0 Fehlschläge, max. min. \(p=383\).
- Methode B (unabhängig, set-membership): `06_verifikation/ergebnis_set_N200000.txt` — gleiche Zählung, 0 Fehlschläge, gleiches max. min. \(p=383\).
- Tests: `python 06_verifikation/test_goldbach.py` → `ALLE TESTS OK` (2026-09-29).
- Partitionen \(4\le n\le 100\): `04_rechnungen/partitionen_klein.txt`.
- Heuristik: `04_rechnungen/singular_series_stichprobe.txt`.

Diese Checks **ersetzen keinen Beweis**.

## Offene Lücke (der eigentliche Blocker)

Für die binäre Form liefert die Kreismethode auf den Minor Arcs **keine** hinreichend starke Abschätzung, um \(r_2(n) > 0\) für alle großen geraden \(n\) zu erzwingen. Siebmethoden erreichen \(p+P_2\), nicht durchgängig \(p+p'\). Kein hier dokumentierter Weg schließt diese Lücke.

## Nächster Arbeitsschritt

1. Montgomery–Vaughan-Original (*Acta Arith.* 27) seitenweise gegenlesen, \(\delta\) notieren.
2. Kein Vorstoß als „Beweis von \(G_{\mathrm{bin}}\)“, solange Minor Arcs bzw. \(P_2\to P_1\) offen sind.
3. Gegenprüfung: beide Python-Läufe plus `test_goldbach.py`.

## Leseordnung für Gegenprüfung

1. Dieses File  
2. `README.md`  
3. `00_laborjournal/JOURNAL.md`  
4. `01_problemstellung/FORMULIERUNG.md`  
5. `07_publikationsentwurf/manuskript.md`  
6. Verifikation reproduzieren: `python 06_verifikation/goldbach_check.py 200000`
