# Beat the room

### Rätsel

1. Schlüssel umdrehen
2. Überwachung zu Verdunklung
   Die Kamera des Pi's wird aktiviert und wartet auf geringen Lichteinfall. Sobald beispielsweise die Hand vor die Kamera gelegt wird, beginnt das dritte Rätsel
3. Radio FM LichtHinweis.
   Radio wird gespielt; die interact-Methode wartet auf die HEX Eingabe
4. Protokol zu Penny
5. Ubrella bis Klicker Eingabe

## Basic Rätsel-Klasse

Jedes Rätsel besteht aus:

#### Einer Init-Methode:

Hier werden alle benötigten Sensoren etc. initialisiert.

#### Einer interact-Methode:

Diese Methode prüft, ob das Rätsel gelöst wurde. Solange dies nicht geschehen ist, läuft diese Methode.
Wenn das Rätsel gelöst wurde, wird die interact-Methode abgebrochen/beendet und die deinit-Methode aufgerufen.

#### Einer Deinit-Methode:

Hier werden alle in der Init-Methode initialisierten Sensoren etc. deinitialisiert.
