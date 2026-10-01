# Verifikation

## Kommando

```text
python 06_verifikation/goldbach_check.py 200000
```

Optionales Argument: gerade Obergrenze \(N\ge 4\).

## Semantik

- Eingabe: \(N\).
- Algorithmus: Eratosthenes bis \(N\); für jedes gerade \(n\in[4,N]\) existenzieller Test auf \(p+q=n\).
- Ausgabe: `ergebnis_N{N}.txt`, plus `04_rechnungen/partitionen_klein.txt` und `singular_series_stichprobe.txt`.
- Exitcode 0: keine Fehlschläge im Intervall; Exitcode 1: Gegenbeispiel gefunden (würde \(G_{\mathrm{bin}}\) widerlegen).

## Zweite Methode

```text
python 06_verifikation/goldbach_check_set.py 200000
python 06_verifikation/test_goldbach.py
```

Methode B: Primzahl-`set`, Mitgliedschaft \(n-p\). Erwartet: gleiche Fehlschlagzahl 0, gleiches max. min. \(p=383\) für \(N=200000\).

## Was die Läufe vom 2026-09-29 zeigten

Siehe `ergebnis_N200000.txt` und `ergebnis_set_N200000.txt`: je 99999 gerade \(n\), 0 Fehlschläge, Python 3.14.7. Tests: `ALLE TESTS OK`.
