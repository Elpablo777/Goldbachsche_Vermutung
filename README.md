# Forschungsarchiv: Goldbachsche Vermutung

Dieses Verzeichnis ist das **einzige** Arbeitsprodukt für die Aufgabe, die binäre Goldbach-Aussage nach Publikationsstandards zu behandeln. Andere Agenten sollen hier lesen, rechnen und gegenprüfen — nicht aus Chatverläufen.

## Ehrliche Kernaussage

**Die binäre Goldbachsche Vermutung ist hier nicht bewiesen.**  
Sie ist in der Zahlentheorie weiterhin ein offenes Problem. Dieses Archiv trennt:

- **Theoreme** (mit Literaturbeleg),
- **endliche Verifikationen** (mit reproduzierbarem Code),
- **Heuristiken und Vermutungen** (explizit so markiert),
- **verworfene oder nicht gewählte Wege**.

Ein erfundener oder lückenhafter „Beweis“ wäre wissenschaftlich wertlos und wird nicht abgeliefert.

## Verzeichnisstruktur

| Pfad | Inhalt |
|---|---|
| `STATUS.md` | Immer zuerst lesen: bewiesen / offen / Blocker |
| `00_laborjournal/` | Zeitliche Spur: Recherche, Rechnung, Prüfung |
| `01_problemstellung/` | Definitionen, Notation, genaue Aussage |
| `02_literatur/` | Zitate, was folgt, was nicht folgt |
| `03_methoden/` | Methodeninventar, gewählt vs. verworfen |
| `04_rechnungen/` | Explizite Partitionen, Heuristik-Vergleich |
| `05_beweisentwuerfe/` | Lückenanalyse, keine Pseudo-QED |
| `06_verifikation/` | Python-Sieb, reproduzierbarer Lauf |
| `07_publikationsentwurf/` | Manuskript im Paper-Stil |
| `LICENSE` | CC BY-NC-SA 4.0 (keine kommerzielle Nutzung) |
| `CODE_OF_CONDUCT.md` | Zusammenarbeit / Gegenprüfung |
| `SECURITY.md` | Keine Geheimnisse; nur Mathematik/Code |
| `PATCHLOG.md` | Änderungshistorie |

## Reproduktion (Gegenprüfung, 2 Minuten)

```text
python 06_verifikation/goldbach_check.py 200000
python 06_verifikation/goldbach_check_set.py 200000
python 06_verifikation/test_goldbach.py
```

Erwartet: 99999 gerade Zahlen in \([4, 200000]\), 0 Fehlschläge, Tests OK.  
Das beweist Goldbach **nicht** für alle geraden \(n\).

Elementare geschlossene Sätze: `01_problemstellung/ELEMENTARE_SAETZE.md`.

## Repository & Aktualität

- Spiegel/Arbeitsstand: https://github.com/Elpablo777/Goldbachsche_Vermutung (bei jedem Meilenstein commit+push).
- Große Witness-Dateien (`06_verifikation/witnessen/*.bin`) liegen nur lokal und sind regenerierbar; sie werden wegen der GitHub-Größenlimits nicht gepusht (siehe `.gitignore` und `06_verifikation/ANLEITUNG.md`).

## Lizenz

CC BY-NC-SA 4.0 — Nutzung und Weitergabe nichtkommerziell, mit Namensnennung und gleicher Lizenz. Primärquellen Dritter bleiben bei deren Rechteinhabern.
