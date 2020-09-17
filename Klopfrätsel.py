import time
import beat_the_room
import RPi.GPIO as GPIO


class Puzzle1(beat_the_room.Puzzle):

    def init(self):
        # Annika und Johann Versuch  zum Klopfrätsel
        # Sollte einmaliges Klopfen erkennen
        # hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(
            self, "test.avi"), beat_the_room.make_hint(self, "hinweis2.avi")]
        # print("Init(42)")
        # INITIALISIERE SENSOREN / HARDWARE
        global GPIO_PIN = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def interact(self):
        print("interacting(42)")
        GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING,
                              callback=self.lösen, bouncetime=1000)
        # time.sleep(10)
        # sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        while self.solved == False:
            time.sleep(1)

        print("Fertig(42)")

    def lösen(self):
        self.solved = True

    def deinit(self):
        print("deinitlasing(42)")
        # DEINITIALISIERE SENSOREN / HARDWARE
        GPIO.cleanup()


test = True
if test:
    Puzzle1.init()
    time.sleep(1)
    Puzzle1.interact()
    print("succsess")
    Puzzle1.deinit()
