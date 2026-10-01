# Verifikation

## Methodenübersicht

| Methode | Datei | Sprache/Ansatz | unabhängig |
|---|---|---|---|
| A | `goldbach_check.py` | Python: Sieb-Liste + lineare Suche | — |
| B | `goldbach_check_set.py` | Python: Hash-Set-Membership | ja (zu A) |
| C | `goldbach_check_np.py` | Python/NumPy: Vektor-Sieb + Restmengen-Elimination | ja (zu A/B) |
| D | `go/goldbach_check.go` | Go: ungerades Bitsieb, parallel, eigene Witness-Datei | ja (zu A/B/C) |
| V | `verify_witnesses.py` | Python/NumPy: liest Witness-Datei, prüft CRC/Gültigkeit/Minimalität | Gegenprüfer zu D |

Alle Methoden: exakte Integer-Arithmetik, keine Floating-Point-Entscheidungen
(Floating Point nur in der als Heuristik markierten singulären Reihe).

## Kommandos (2-Minuten-Gegenprüfung)

```text
python 06_verifikation/goldbach_check.py 200000
python 06_verifikation/goldbach_check_set.py 200000
python 06_verifikation/goldbach_check_np.py 200000
python 06_verifikation/go/goldbach_check.exe -N 200000   # nach `go build` (siehe unten)
python 06_verifikation/test_goldbach.py
```

Erwartet: je 99999 gerade n in [4, 200000], 0 Fehlschläge, max. min-p = 383,
Tests OK. Das beweist Goldbach **nicht** für alle geraden n.

## Große Läufe (Stand 2026-10-01)

| N | Methode | Ergebnis | Ergebnisdatei |
|---|---|---|---|
| 10^7 | C | 4 999 999 gerade n, 0 Fehlschläge, max min-p = 751 | `ergebnis_np_N10000000.txt` |
| 10^7 | A, B | identisch (Legacy-Gegenprobe: 7,7 s / 4,0 s) | `ergebnis_N10000000.txt`, `ergebnis_set_N10000000.txt` |
| 10^7 | D | identisch; Witness-Datei **byte-identisch** zu Methode C | `ergebnis_go_N10000000.txt` |
| 10^8 | D (lokal) | 49 999 999 gerade n, 0 Fehlschläge, max min-p = 1093 | `ergebnis_go_N100000000.txt` |
| 10^8 | V (v1+v2) | alle Witness gültig + Minimalität bestätigt | `verify_report_N100000000.txt`, `verify2_report_N100000000.txt` |
| 10^9 | D (GitHub Actions, ubuntu-latest, Go 1.27.1, 4 vCPU) | **499 999 999 gerade n, 0 Fehlschläge, max min-p = 1789**, 13,2 s Rechenzeit | `ergebnis_go_N1000000000.txt` (vom CI-Bot committet) |
| 10^9 | V2 (lokal, vollständig) | **alle 499 999 999 Witness gültig und minimal**, CRC ok | `verify2_report_N1000000000.txt` |

Witness-Dateien liegen (nur lokal, regenerierbar) in `06_verifikation/witnessen/`:

- `witness_go_N100000000.bin`, 51 602 366 Bytes,
  SHA256 `2b540ea5e736b3bc4cbe1e7ba00c23ad4e9e803faf86b37c00b96778cd93dbd8`.
- `ci_N1000000000/witness_N1000000000.bin` (CI-Artefakt-Download), 524 383 817 Bytes,
  SHA256 `db9b61ac5f4c904b148181be9a1c67ca459a552c5c38964a1d5999afb9f76b99`
  (identisch zur CI-Aufzeichnung `sha256_N1000000000.txt`).
- Format `GBWIT1`: Zeile 1 `GBWIT1`, Zeile 2 `N`, dann LEB128-Varints des
  minimalen p für n = 4, 6, …, N (in dieser Reihenfolge), dann 4 Bytes
  CRC32 (IEEE, little-endian) über den Payload.

## CI (GitHub Actions) — kostenlose Rechenleistung

- Workflow: `.github/workflows/goldbach.yml`. Triggert bei Push auf `06_verifikation/go/**` oder manuell (`gh workflow run goldbach-verification -f N=...`).
- Schritte: Build → Selbsttest N=200000 (muss „0 Fehlschläge" und „max min-p 383" melden, sonst Abbruch) → großer Lauf (Default N=10^9) → SHA256 → Artefakt-Upload (90 Tage) → Auto-Commit der kleinen Ergebnisdatei ins Repo (github-actions[bot]).
- Limits (recherchiert, `02_literatur/KI_FORMAL_RECHENLEISTUNG_2026-10.md` Quellen 14–16): public repo kostenlos, 6 h/Job, ubuntu-latest 4 vCPU/16 GB/14 GB SSD.
- **Vertrauensgrenze (explizit, Lean-Vorbild):** der CI-Lauf ist ein Zertifikat, kein Vertrauensakt — er gilt nur zusammen mit (a) lokal reproduziertem Byte-Identitätsnachweis desselben Binaries bei 10^7/10^8, (b) CI-Selbsttest 383, (c) vollständiger lokaler Gegenverifikation der heruntergeladenen Witness-Datei durch `verify_witnesses2.py` (erfolgt, siehe Tabelle oben), (d) protokollierten SHA256/CRC32 und Umgebungsversionen.

## Verifier v2 (für große N)

```bash
python 06_verifikation/verify_witnesses2.py 1000000000 \
    06_verifikation/witnessen/ci_N1000000000/witness_N1000000000.bin
```

int32-Arithmetik + gechunkter vektorisierter LEB128-Decoder; prüft Header/CRC/
Tokenzahl, JEDES Witness (Existenz) und die komplette Minimalität via
Methode-C-Neuberechnung. Vor Erstbenutzung an der 10^8-Datei validiert
(identische Resultate zu v1). Gesamtlaufzeit für 10^9: ~113 s.

## Go bauen und große Läufe wiederholen

```bash
cd 06_verifikation/go
go build -o goldbach_check.exe .
./goldbach_check.exe -N 100000000 -witness ../witnessen/witness_go_N100000000.bin \
    -out ../ergebnis_go_N100000000.txt
cd ../.. && python 06_verifikation/verify_witnesses.py 100000000 \
    06_verifikation/witnessen/witness_go_N100000000.bin
```

## Umgebung der Läufe vom 2026-10-01

- Python 3.14.8, NumPy 2.4.3, Windows (win32), 12 logische Kerne.
- Go 1.27.0 windows/amd64, GOMAXPROCS 12.
- Laufzeiten: C@10^7 ≈ 0,6 s; D@10^8 ≈ 0,72 s (Berechnung, ohne Witness-Write);
  V@10^8 ≈ 18 s.
- Exitcode 1 = Gegenbeispiel gefunden (würde G_bin widerlegen); trat nie auf.

## Triangulation primesieve (dritter Primzahlgenerator)

```bash
winget install primesieve          # v12.16, BSD-2-Clause
"/c/Program Files/primesieve/bin/primesieve.exe" 1000000000 --count=1   # → 50847534
"/c/Program Files/primesieve/bin/primesieve.exe" 999000000 1000000000 --print
```

Abgleich gegen den NumPy-Sieb: `06_verifikation/triangulierung_primesieve.txt`
(π(10⁹) identisch; Segment-Primzahlen identisch — zwei voneinander unabhängige
Sieb-Implementierungen liefern dieselben Primzahlen bis 10⁹).

## Segmentmodus (für große Skalen, Wiederaufnahme)

```bash
cd 06_verifikation/go && go build -o goldbach_check.exe .
./goldbach_check.exe -A 4000002 -N 10000000 -witness seg.bin -out seg_ergebnis.txt
```

`-A` = gerader Segmentstart (Default 4 = Vollbereich). Das Sieb bleibt ein
Voll-Sieb bis N; die Witness-Suche läuft nur im Segment [A, N] — Grundlage
für CI-Matrix-Parallelläufe (z. B. 10 × 10^9-Segmente bis 10^10).
Witness-Formate: `GBWIT1` (A=4, unverändert) und `GBWITSEG1` (A>4, Kopfzeile
mit A). Getestet (2026-10-01): A=4-Witness-Datei **byte-identisch** zum
Voll-Lauf; Segment-Payload identisch mit dem Tokenfenster des Voll-Laufs.
**Offen bei Archivierung:** Matrix-Workflow und GBWITSEG1-Unterstützung im
Verifier (`verify_witnesses2.py`) — bewusst nicht als fertig deklariert.

## Semantik / Beweisstatus

- Eingabe: gerade Obergrenze N ≥ 4.
- „Fehlschläge = 0“ ⇒ Aussage gilt für alle geraden n in [4, N] (endliche
  Exhaustion, kein Induktionsschritt).
- Daraus folgt **nicht** die Aussage für alle geraden n ≥ 4. Kein Lauf dieses
  Ordners ist ein Beweis der Goldbachschen Vermutung.
