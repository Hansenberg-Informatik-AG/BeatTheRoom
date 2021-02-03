# Beat the room

## Aufgaben
Story festlegen
Story Umsetzung: Video, Texte, Materialen, Audios, Hilfestellungen
Rätsel fertigstellen und anpassen
Raumaufteilung

## Rätsel

Story Konzept STANLEY
### Zu Beginn vorhanden: 
Schlüssel, Lautsprecherbox, Sicherheitshinweispapier, Umbrella-Rechnung (im Fach?), Radio-Taschenlampe + Papier, Brett
### Rätsel 1: Schlüssel
Schlüssel umdrehen
### Rätsel 2: Kamera
Überwachung zu Verdunklung
Die Kamera des Pi's wird aktiviert und wartet auf geringen Lichteinfall. Sobald beispielsweise die Hand vor die Kamera gelegt wird, beginnt das dritte Rätsel
### Rätsel 3: Radio
Radio FM LichtHinweis
-->	Gibt Geländecode (4028) aus
Radio wird gespielt;
### Rätsel 4: Code ins Numpad eingeben
die interact-Methode wartet auf die HEX Eingabe
-->	Screenshot der Webseite wird gezeigt (IP-Adresse)
### Rätsel 5: Webseite (über hansenberg.info server)
a.	IP-Adresse im Handy aufrufen, um auf Webseite zu gelangen
b.	Screenshot sieht anders aus --- Fehler/Unterschiede suchen -> neues Rätsel?
c.	Auf Webseite Benutzername und Passwort eingeben („hacken“)
- Counter mit Fehlversuchen-Hinweis: können Sie lesen?
-->	Führt zum Penny Video
### Rätsel 6: Penny Klopfzeichen
=> Das Lösen öffnet ein Fach mit (weiteren Hinweisen, Rätseln…)
-> Weitere Hinweise, Überleitung zur Mail?
### Rätsel 7: Mail an Frau von Zitzewitz schreiben
=> Automatische Antwort mit Rückverweis auf das Sicherheitsstufenblatt
### Rätsel 8: Sicherheitsstufenblatt („schlecht gedruckt“ – muss auf bestimmte Art geknickt   werden)
       => entstandener augmented reality code auf Webseite scannen (vllt Verweis auf Umdrehen?)
=> Ausgabe eines 4-stelligen Zahlencodes für das Seitenfach mit einem Schlüssel
=> Schlüssel für Blaue Kassenbox => darin liegt der Ausweis (und UV-Lampe?)
### Rätsel 9: Umbrella-Rätsel
Ubrella bis Klicker Eingabe
       => wir erhalten einen Code für die Klicker

## Basic Rätsel-Klasse

Jedes Rätsel besteht aus:

#### Einer Init-Methode:

Hier werden alle benötigten Sensoren etc. initialisiert.

#### Einer interact-Methode:

Diese Methode prüft, ob das Rätsel gelöst wurde. Solange dies nicht geschehen ist, läuft diese Methode.
Wenn das Rätsel gelöst wurde, wird die interact-Methode abgebrochen/beendet und die deinit-Methode aufgerufen.

#### Einer Deinit-Methode:

Hier werden alle in der Init-Methode initialisierten Sensoren etc. deinitialisiert.


# Story, evtl. die finale

Süßigkeiten in einem Raum? Nutella/ Nuss-Nougat-Creme
Schüler brechen nachts in Schulgebäude (Pakhos Büro?, am Fenster) ein (Noten ausbessern)/ 21 Uhr, man muss bis 22 Uhr zurücksein

Stanley ist schon an --> Sirene leuchtet schon / fängt an zu leuchten, wenn die Tür ins Schloss fällt (Schlüssel zum ausmachen der Sirene)
Stanley fährt hoch (Vorstellung "Stromversorgung hergestellt", "Gesichtserkennung und automatische Speicherung aktiviert!!" oder einfach Video mit recording in der Ecke)
Kamera schaltet sich an, man sieht sich selbst auf dem Bildschirm (Kamera-Rätsel --> Abdeckung der Kamera --> "visuelles tracking nicht möglich, ändere Strategie, stelle letzte Ausioaufnahme zu den Soz-Päds... speicher korrupiert, gebe letzte Audionachricht wieder")

Rauschen (durch Radiorätsel erfährt man, Programmierer im System sind (Hörner und Leppla), welche Stanley "vermeidlich" als totale Überwachung programmiert haben)
Wichtige Wörter um zu verstehen, dass es nicht so ist sind aus gerauscht --> totale Überwachung, Code ist der übliche um aufs Gelände zu kommen (mit rauschen)

"Der Code wurde korrekt eingegeben, automatische Weiterleitung zu Website erfolt, Freischaltung des Tresors jetzt möglich" --> keine Tastatur und Maus --> IP-Adresse im Handy eingeben (Benutzer und Passwort eingeben)

Wargame(Idee) --> Stanley von Hörner (und Leppla) (am Anfang nich bekannt) programmiert, selbstlernend (Schüler sollen sich nicht mehr austragen müssen, inklusive Gesichtserkennung) 
--> Leppla und Hörner erst als die bösen, dann schlussendlich nur zu dumm gewesen Stanley richtig zu programmieren
--> teile aus gesprochenen Sätzen der "Programmierer" werden ausgeraucht --> dasgegenteil kommt rüber (Hörner und Leppla werden als böse dargestellt)

benötigen einen "guten" Stanley-Namen, welcher durch rausstreichen von Wörtern böse klingt

Schüler wollen versuchen, die Aufnahme ihres Einbruchs zu löschen --> dafür muss Stanley ausgeschaltet werden

Idee für das Ende: wir können STANLEY nicht vor Ort ausschalten und müssen deshalb die Zentrale ausfindig machen (NFC-Chip-Rätsel mit Karte-Koordinaten etc., vllt Informatikraum??) 

### Konzept von den Rätseln

Story Konzept STANLEY
### Zu Beginn vorhanden: 
Lautsprecherbox, Sicherheitshinweispapier, Umbrella-Rechnung (im Fach?), Radio-Taschenlampe + Papier, Brett
## Rätsel 1: Schlüssel
(verzerrte Roboterstimme von STANLEY zu hören) 
Herzlich Willkommen an der ISH, der weltbesten KI überwachten Internatsschule
Schloss Hansenberg, meinem Meisterwerk! Ich bin Stanley und dieser Bereich fällt mit sofortiger Wirkung unter meine Zuständigkeit. Ab sofort kehrt hier Disziplin ein!
Danke, dass Sie mich gebootet haben.
Überwachungssystem läuft in 3 2 1 (Kamera einschalten, Hochfahr/Aktivierungs Sound)
Zur Prozessoptimierung werden Entlassungspapiere an alle Sozialpädagogen und Lehrer verschickt.
-	rote LEDs?
--> zweites Schlüsselrätsel?????? --> zu Anfang zwei Schlüssel an einem Bund, man muss darauf kommen, dass der zweite Schlüssel am Bund noch für was anderes ist
### Rätsel 2: Kamera
(Stimme STANLEY) 
Visuelle Überwachung im Kontrollzentrum deaktiviert.
Gefahrenquelle wurde entdeckt. 
Sicherheitssystem wird aktiviert. 
Gefahrenstufe wird erhöht.
-	Sirene!?
## Rätsel 3: Radio
-->	Gibt Geländecode (4028) aus
## Rätsel 4: Code ins Numbed eingeben
-->	Screenshot der Webseite wird gezeigt (IP-Adresse)
## Rätsel 5: Webseite (über hansenberg.info server)
a.	IP-Adresse im Handy aufrufen, um auf Webseite zu gelangen
b.	Screenshot sieht anders aus --- Fehler/Unterschiede suchen -> neues Rätsel?
c.	Auf Webseite Benutzername und Passwort eingeben („hacken“)
- Counter mit Fehlversuchen-Hinweis: können Sie lesen?
-->	Führt zum Penny Video
## Rätsel 6: Penny Klopfzeichen
=> Das Lösen öffnet ein Fach mit (weiteren Hinweisen, Rätseln…)
> Überleitung zur Mail?
## Rätsel 7: Mail an Frau von Zitzewitz schreiben
=> Automatische Antwort mit Rückverweis auf das Sicherheitsstufenblatt
## Rätsel 8: Sicherheitsstufenblatt („schlecht gedruckt“ – muss auf bestimmte Art geknickt   werden)
       => entstandener augmented reality code auf Webseite scannen (vllt Verweis auf Umdrehen?)
=> Ausgabe eines 4-stelligen Zahlencodes für das Seitenfach mit einem Schlüssel
=> Schlüssel für Blaue Kassenbox => darin liegt der Ausweis (und UV-Lampe?)
9)   Rätsel 9: Umbrella-Rätsel
       => wir erhalten einen Code für die Klicker
 
### Weitere Rätselideen, bisher offen:
Schlussrätsel:
Wo sitzt der unbekannte Hacker?
--> Blatt/Album mit Bildern, die auf Städte/Länder verweisen
--> Landkarte/Atlas => Koordinaten? Linien ziehen, Schnittpunkt?

--> falls Landkarte (Stadtnamen – an rote Aufkleber schreiben, die anzeigen, was man nicht anfassen soll – auch andersfarbige? Zur Verwirrung, nur Rot darf man nicht anfassen?) auf Stanley NFC-Sensor hinter dem Ort => Chip davorhalten = Stanley schaltet sich aus und wir haben gesiegt?!
              --> extra Brett (mit Landkarte/Kabel (iwo verstecken)/dongel zum aktivieren  -uv-licht?) über VGA an Stanley… im Brett dann NFC-Chips verarbeiten

Hinweis z.B. kryptisches Blatt in blauer Box sind Codes/Zahlen, die einem in einem Buch zu bestimmten Wörtern führen… -> ergebnis-wörter stellen Hinweis für neues Rätsel dar?

Leuchtzahlen? -rätsel? (Sebastian)----strahlt mit abstand hinweise für bestimmtes Wort/Zahl aus?
Youthlessbox???
Uv-licht und lampe!?
Zweiter monitor? Zweiter pi! --- brille?! (Anne)


S	security / secure
T	terminal / teacher
A	against / and / anti / automation 
N	non / no / natural
L	learning
E	excessive / experience / evil
Y	youth

Secure Termination of All Non-Learning Embarrassing Youths

(im Akronym neues Rätsel?)
