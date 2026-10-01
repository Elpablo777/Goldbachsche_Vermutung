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
| 10^7 | D | identisch; Witness-Datei **byte-identisch** zu Methode C | `ergebnis_go_N10000000.txt` |
| 10^8 | D | 49 999 999 gerade n, 0 Fehlschläge, max min-p = 1093 | `ergebnis_go_N100000000.txt` |
| 10^8 | V | alle Witness gültig + Minimalität bestätigt | `verify_report_N100000000.txt` |

Witness-Dateien liegen (nur lokal, regenerierbar) in `06_verifikation/witnessen/`:

- `witness_go_N100000000.bin`, 51 602 366 Bytes,
  SHA256 `2b540ea5e736b3bc4cbe1e7ba00c23ad4e9e803faf86b37c00b96778cd93dbd8`.
- Format `GBWIT1`: Zeile 1 `GBWIT1`, Zeile 2 `N`, dann LEB128-Varints des
  minimalen p für n = 4, 6, …, N (in dieser Reihenfolge), dann 4 Bytes
  CRC32 (IEEE, little-endian) über den Payload.

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

## Semantik / Beweisstatus

- Eingabe: gerade Obergrenze N ≥ 4.
- „Fehlschläge = 0“ ⇒ Aussage gilt für alle geraden n in [4, N] (endliche
  Exhaustion, kein Induktionsschritt).
- Daraus folgt **nicht** die Aussage für alle geraden n ≥ 4. Kein Lauf dieses
  Ordners ist ein Beweis der Goldbachschen Vermutung.
