# Problemstellung und Notation

## Historische Quelle

Christian Goldbach an Leonhard Euler, 7. Juni 1742 (übliche moderne Lesart).  
Die heute übliche **starke / binäre** Form ist eine Präzisierung Eulers.

## Definitionen

- \(\mathbb{P}\): Menge der Primzahlen \(\{2,3,5,7,\ldots\}\).
- Eine **Goldbach-Partition** von \(n\) ist ein Paar \((p,q)\in\mathbb{P}\times\mathbb{P}\) mit \(p+q=n\). Wir schreiben oft \(p\le q\).
- \(r_2(n)\): Anzahl **geordneter** Paare \((p,q)\) mit \(p+q=n\), \(p,q\in\mathbb{P}\).
- \(G_2(n)\): Anzahl **ungeordneter** Paare mit \(p\le q\). Es gilt \(r_2(n)=2G_2(n)\) falls \(n\neq 2p\), und \(r_2(n)=2G_2(n)-1\) falls \(n=2p\) für ein \(p\in\mathbb{P}\).

## Zielaussage (stark / binär / even Goldbach)

**Aussage \(G_{\mathrm{bin}}\).**  
Für jede gerade ganze Zahl \(n\ge 4\) existieren \(p,q\in\mathbb{P}\) mit \(p+q=n\).

Äquivalent: \(G_2(n)\ge 1\) für alle geraden \(n\ge 4\).

## Schwache / ternäre / odd Goldbach

**Aussage \(G_{\mathrm{ter}}\).**  
Für jede ungerade ganze Zahl \(n\ge 7\) existieren \(p,q,r\in\mathbb{P}\) mit \(p+q+r=n\).

(Manchmal: jedes ungerade \(n>5\). Die Fälle \(n=7,9,\ldots\) sind elementar prüfbar.)

**Logische Beziehung (elementar, kein tiefer Satz):**  
Aus \(G_{\mathrm{bin}}\) folgt \(G_{\mathrm{ter}}\) für \(n\ge 7\), denn \(n-3\) ist gerade \(\ge 4\), also \(n-3=p+q\) und \(n=3+p+q\), bzw. analog mit \(2\) wo nötig.  
Die Umkehrung gilt **nicht**.

## Was „Lösung“ hier bedeuten würde

Ein Beweis von \(G_{\mathrm{bin}}\) im Sinne einer Veröffentlichung muss:

1. die Aussage quantorenpräzise formulieren,
2. nur bereits bewiesene Hilfssätze oder vollständig ausgeführte Argumente verwenden,
3. jede Abschätzung mit explizitem Gültigkeitsbereich versehen,
4. Computeranteile als endliche, reproduzierbare Checks ausweisen, nicht als Ersatz für den unendlichen Rest.

**In diesem Archiv ist Bedingung 2–4 für \(G_{\mathrm{bin}}\) nicht erfüllt.** \(G_{\mathrm{ter}}\) wird als in der Literatur bewiesen **zitiert**, hier nicht neu bewiesen.
