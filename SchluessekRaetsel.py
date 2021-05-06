import time
import beat_the_room
import os
import RPi.GPIO as GPIO


class SchluesselRaetsel(beat_the_room.Puzzle):

    def init(self):
        # hinweis filmdatei
        # die Rätsel sind linear
        os.system("tvservice -o")
        self.hints = [beat_the_room.make_hint(
            self, "test.avi"), beat_the_room.make_hint(self, "hinweis2.avi")]
        # Rätsel erstellt von: Leo Wenzel

        # INITIALISIERE SENSOREN / HARDWARE
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.IN)

    def interact(self):
        anfang = GPIO.input(21)
        print("--- GPIO zu Beginn ---")
        print(anfang)
        # sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        while not self.solved:
            self.solved = GPIO.input(21) != anfang

    def deinit(self):
        print("deinitlasing(42)")
        os.system("tvservice -p")
        GPIO.cleanup()
