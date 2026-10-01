# Patchlog

## 2026-10-01 — Archiv v2 (Repository)

- Neu: GitHub-Repository https://github.com/Elpablo777/Goldbachsche_Vermutung (öffentlich), erstes Push von v0–v2.
- Neu: `.gitignore` (Buildartefakte, große regenerierbare Witness-Dateien).
- Neu (geplant/laufend): Methode C (NumPy) bis 10^7, Methode D (Go) bis 10^8 mit Witness-Datei + unabhängigem Verifier, Statistik (max. min. p(n), Rekordhalter, Goldbach-Komet), elementare Sätze 5–6, Literatur-Update `02_literatur/UPDATE_2026-10.md` (Hintergrundagent).
- Inhaltlich: G_bin bleibt **offen**; keine Statusänderung.

## 2026-09-29 — Archiv v0

- Neu: gesamte Ordnerstruktur `00_`–`07_`, `README.md`, `STATUS.md`, `LICENSE` (CC BY-NC-SA 4.0), `CODE_OF_CONDUCT.md`, `SECURITY.md`.
- Neu: `06_verifikation/goldbach_check.py`.
- Lauf: `python 06_verifikation/goldbach_check.py 200000` → 0 Fehlschläge, siehe `06_verifikation/ergebnis_N200000.txt`.
- Inhaltlich: binäres Goldbach **nicht** als bewiesen markiert; Helfgott/Chen/Vinogradov/OHP14 zitiert; Lückenanalyse der Kreismethode.

## 2026-09-29 — Archiv v1

- Neu: `01_problemstellung/ELEMENTARE_SAETZE.md` (lückenlose elementare Sätze).
- Neu: `05_beweisentwuerfe/EXCEPTIONAL_SET.md`.
- Neu: `06_verifikation/goldbach_check_set.py`, `test_goldbach.py`, `ergebnis_set_N200000.txt`.
- Tests grün; Methode B bestätigt Methode A bis \(N=200000\).
- Literatur: Estermann, Montgomery–Vaughan, explizites Chen (Yamada / BJS).
