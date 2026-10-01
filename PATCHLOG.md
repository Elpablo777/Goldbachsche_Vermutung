# Patchlog

## 2026-10-01 — Archiv v4: 10^9-Verifikation (CI + volle Gegenprüfung), Sätze 5–7, Literatur/KI-Update

- Neu: Methode C `06_verifikation/goldbach_check_np.py` (NumPy, vektorisiert); Lauf 10^7: 0 Fehlschläge, max min-p 751.
- Neu: Methode D `06_verifikation/go/goldbach_check.go` (Go, ungerades Bitsieb, parallel, Witness-Datei GBWIT1); 10^7 (byte-identisch zu C), 10^8 lokal (max min-p 1093), **10^9 auf GitHub Actions** (kostenloser Runner, 13,2 s Rechenzeit, max min-p 1789, 0 Fehlschläge).
- Neu: Verifier `verify_witnesses.py` (v1) und `verify_witnesses2.py` (int32 + gechunkter Varint-Decoder); v2 vollständig validiert an 10^8, dann **vollständige Gegenverifikation der 10^9-CI-Witness-Datei**: alle 499 999 999 Witness gültig und minimal (SHA256 db9b61ac…dbd8).
- Neu: `.github/workflows/goldbach.yml` (CI: Selbsttest 383, großer Lauf, Artefakte, Auto-Commit der Ergebnisdatei).
- Neu: `01_problemstellung/ELEMENTARE_SAETZE.md` Sätze 5–7 (Bertrand/Erdős mit Produktlemma, O(log n)-Zerlegung, Siebkorrektheit) + Maschinenchecks in `test_goldbach.py` (ALLE TESTS OK).
- Neu: `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md` (28 Quellen: Lean-4-Formalisierung ternäre Goldbach; KI hat G_bin nicht angegangen; GitHub-Actions-Limits; primesieve; Pintz δ=0,28 bester expliziter Ausnahmemengen-Exponent; Chen v6 „to appear IJNT").
- Aktualisiert: `STATUS.md`, `README.md`, `06_verifikation/ANLEITUNG.md`, `05_beweisentwuerfe/EXCEPTIONAL_SET.md`, `07_publikationsentwurf/manuskript.md`.
- Inhaltlich: G_bin bleibt **offen**; keine Statusänderung.

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
