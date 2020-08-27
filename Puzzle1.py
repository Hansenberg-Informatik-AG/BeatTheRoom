
import time
import beat_the_room


class Puzzle1(beat_the_room.Puzzle):

    def init(self):
        # hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(
            self, "test.avi"), beat_the_room.make_hint(self, "hinweis2.avi")]
        # print("Init(42)")
        # INITIALISIERE SENSOREN / HARDWARE

    def interact(self):
        print("interacting(42)")
        # time.sleep(10)
        # sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        self.solved = True
        print("Fertig(42)")

    def deinit(self):
        print("deinitlasing(42)")
        # DEINITIALISIERE SENSOREN / HARDWARE
        # GPIO.cleanup() etc.
