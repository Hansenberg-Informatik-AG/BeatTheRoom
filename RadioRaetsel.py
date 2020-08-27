
import RPi.GPIO as gpio
import time
import beat_the_room.Puzzle

import fm

class RadioPuzzle(beat_the_room.Puzzle):

    def init(self):
        #hinweis filmdatei
        # die Rätsel sind linear
        #Rätsel:
        #1 Schlüsseldrehen und anlassen. Die Zeit läuft wenn das erste Rätsel beendet ist
        #2 Überwachung zu Verdunklung. Kamera an -> geringer Lichteinfall
        #3 Radio FM LichtHinweis. Radio -> HEX Eingabe
        #4 Protokol zu Penny
        #5 Umbrella bis Klicker Eingabe
        
        
        
        self.hints = [beat_the_room.make_hint(self, "test.avi"),beat_the_room.make_hint(self,"hinweis2.avi")]
        print("Init(Radio)")


        gpio.setmode(gpio.BCM)

        matrix = [['1','2','3','A'],
            ['4','5','6','B'],
            ['7','8','9','C'],
            ['*', '0', '#','D']]

        spalte = [16, 20, 21,12]
        zeile = [6, 13, 19, 26]

        for j in range(len(spalte)):
            gpio.setup(spalte[j], gpio.OUT)
            gpio.output(spalte[j], 1)

        for i in range(len(zeile)):
            gpio.setup(zeile[i], gpio.IN, pull_up_down = gpio.PUD_UP)

        fm.start_radio()

        
    def interact(self):
        print("interacting(42)")
        lastNumbers = [0,0,0,0]
        while True:
            for j in range(3):
                gpio.output(spalte[j], 0)
                for i in range(4):
                    if gpio.input(zeile[i]) == 0:
                        benutzerEingabe = matrix[i][j]
                        lastNumbers.pop(0)
                        lastNumbers.append(benutzerEingabe)
                        while gpio.input(zeile[i]) == 0:
                            pass
                        return benutzerEingabe                  
                gpio.output(spalte[j], 1)
        self.solved = True
        print("Fertig(Radio)")

    def deinit(self):
        fm.terminate()
        print("deinitlasing(Radio)")

