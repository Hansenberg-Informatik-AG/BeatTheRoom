# Beat the room

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
Radio FM LichtHinweis (ist das das???)
-->	Gibt Geländecode (4028) aus
Radio wird gespielt; die interact-Methode wartet auf die HEX Eingabe (ist das die Aufgaben??)
### Rätsel 4: Code ins Numpad eingeben
-->	Screenshot der Webseite wird gezeigt (IP-Adresse)
### Rätsel 5: Webseite (über hansenberg.info server)
a.	IP-Adresse im Handy aufrufen, um auf Webseite zu gelangen
b.	Screenshot sieht anders aus --- Fehler/Unterschiede suchen -> neues Rätsel?
c.	Auf Webseite Benutzername und Passwort eingeben („hacken“)
- Counter mit Fehlversuchen-Hinweis: können Sie lesen?
-->	Führt zum Penny Video
### Rätsel 6: Penny Klopfzeichen
=> Das Lösen öffnet ein Fach mit (weiteren Hinweisen, Rätseln…)
> Überleitung zur Mail?
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


### Story 1

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
###Rätsel 2: Kamera
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


 
### Story 2

Anfangssituation?
--zeitdruck erzeugen --- warum wollen wir heraus?
--alarmanlage? Freitag vor ferien?

Zu Beginn hilft uns ein anonymer Hacker (Otto?) – macht sich über uns lustig
Er hat z.B. mit seinem Trojaner den Screenshot abgefangen
Nach dem Öffnen des Fachs ist STANLEY endlich gehackt, doch Otto übernimmt die Kontrolle
Böse/Sirene/absahen?!
Unser Ziel ändert sich vom Hacken, zum Abschalten von Stanley, damit Otto kein Zugriff mehr hat

Story Ende: Nach dem Herausfinden der Koordinaten, kommt ein Video, der die wahren Ottos zeigt, die ihr Leben genießen (Strand, Karibik? Geld?) -letzte Message von Ihnen (Hörner, Leppla? Schiemenz?)
Nach NFC-Chip am richtigen Ort schaltet sich Stanley ab, und das Ziel wurde erreicht



[offizielle Nachrichten-	Sozpäds auf der Straße vor dem Hansenberg, Demonstration]

Warum sind wir eingesperrt? Warum wollen wir raus?
Wer hilft uns?
Was ist unser Ziel?

-andere Schulen übernehmen

## Story 3

progressive Eskalation
--> am Anfang Hansenberg übernehmen
--> andere Schulen im Rheingaugebiet übernehmen
--> "Fehler im Gebiet "Welt" festgestellt, beginne nun Auslöschung der Menschlichen Rasse" --> Prozentleiste --> kurz vor Schluss

### Schlüsselrtätsel
bootet Stanley
"Guten Morgen, beziehe aktuelle globale Daten. Warten Sie bitte einen Moment... (Wartemusik). System erfolgreich gebootet. Einen Moment bitte, ich übernehme nun die Schule. Sozialpädagogen und Lehrer werden nun nicht mehr benötigt"

### Story Idee

Herr Hörner existiert nicht mehr. Herr Hörner hat sich in einer KI verewigt 
