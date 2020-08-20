import time
import beat_the_room
import RPi.GPIO as GPIO


class SchluesselRaetsel(beat_the_room.Puzzle):

    def init(self):
        #hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(self, "test.avi"),beat_the_room.make_hint(self,"hinweis2.avi")]
        self.id = 42
        print("Init(42)")
        #Rätsel erstellt von: Leo Wenzel




        #INITIALISIERE SENSOREN / HARDWARE
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.IN)

    def interact(self):
        #time.sleep(10)
        #sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        while self.solved == False:
            if GPIO.input(21) == 0:
                self.solved = True

        print("Fertig(42)")

    def deinit(self):
        print("deinitlasing(42)")
        #DEINITIALISIERE SENSOREN / HARDWARE
        #GPIO.cleanup() etc
        GPIO.cleanup()
