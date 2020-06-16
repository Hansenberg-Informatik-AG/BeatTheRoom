
import RPi.GPIO as gpio
import time
import beat_the_room.Puzzle

class Puzzle1(beat_the_room.Puzzle):

    def init(self):
        #hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(self, "test.avi"),beat_the_room.make_hint(self,"hinweis2.avi")]
        #self.id = 42
        #print("Init(42)")


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

        #INITIALISIERE SENSOREN / HARDWARE
        
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
        #time.sleep(10)
        #sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        self.solved = True
        print("Fertig(42)")

    def deinit(self):
        print("deinitlasing(42)")
        #DEINITIALISIERE SENSOREN / HARDWARE
        #GPIO.cleanup() etc.

