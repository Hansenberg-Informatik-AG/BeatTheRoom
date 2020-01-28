


from beat_the_room import Puzzle

class Puzzle1(Puzzle):

    def init(self):
        self.hints = [beat_the_room.make_hint(self, "test.avi")]
        self.activates_ids = [1,4,6]
        self.id = 42

        #INITIALISIERE SENSOREN / HARDWARE
        
    def interact(self):
        while not BEDINGUNG:
            #TUE ETWAS
        self.solved = True

    def deinit(self):
        #DEINITIALISIERE SENSOREN / HARDWARE
