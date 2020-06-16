
import RPi.GPIO as gpio
import time
import beat_the_room.Puzzle

class Puzzle1(beat_the_room.Puzzle):

    def init(self):
        #hinweis filmdatei
        # die Rätsel sind linear
        #Rätsel:
        #1 Schlüsseldrehen und anlassen. Die Zeit läuft wenn das erste Rätsel beendet ist
        #2 Überwachung zu Verdunklung. Kamera an -> geringer Lichteinfall
        #3 Radio FM LichtHinweis. Radio -> HEX Eingabe
        #4 Protokol zu Penny
        #5 Ubrella bis Klicker Eingabe
        
        
        #Display zunächst ausgeschaltet, bzw dunkel
        self.hints = [beat_the_room.make_hint(self, "test.avi"),beat_the_room.make_hint(self,"hinweis2.avi")]
        self.id = 01
        print("Init(01)")
        gpio.setmode(gpio.BCM)
     
        

      
            gpio.setup(spalte[j], gpio.OUT)
            gpio.output(spalte[j], 1)

        for i in range(len(zeile)):
            gpio.setup(zeile[i], gpio.IN, pull_up_down = gpio.PUD_UP)

        #INITIALISIERE SENSOREN / HARDWARE
        
    def interact(self):
        print("interacting(01)")
        self.solved = False
        while not self.solved:
            if gpio.input() ==1:
                self.solved = True
                print("Fertig(01)")
               
               
        #time.sleep(10)
        #sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
       

    def deinit(self):
        print("deinitlasing(01)")
        #DEINITIALISIERE SENSOREN / HARDWARE
        #GPIO.cleanup() etc.

