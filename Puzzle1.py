
import time
import beat_the_room_single

class Puzzle1(beat_the_room_single.Puzzle):

    def init(self):
#hinweis filmdatei
# die Rätsel sind linear
        self.hints = [beat_the_room_single.make_hint(self, "test.avi")]
       
        self.id = 42
        print("Init(42)")




        #INITIALISIERE SENSOREN / HARDWARE
        
    def interact(self):
        print("interacting(42)")
        time.sleep(10)
#sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
        self.solved = True
        print("Fertig(42)")

    def deinit(self):
        print("deinitlasing(42)")
        #DEINITIALISIERE SENSOREN / HARDWARE

