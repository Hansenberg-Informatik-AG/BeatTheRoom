# Beat the room

### Rätsel

Jedes Rätsel besteht aus:

#### Einer Init-Methode:

Hier werden alle benötigten Sensoren etc. initialisiert.

#### Einer interact-Methode:

Diese Methode prüft, ob das Rätsel gelöst wurde. Solange dies nicht geschehen ist, läuft diese Methode.
Wenn das Rätsel gelöst wurde, wird die interact-Methode abgebrochen/beendet und die deinit-Methode aufgerufen.

#### Einer Deinit-Methode:

Hier werden alle in der Init-Methode initialisierten Sensoren etc. deinitialisiert.
