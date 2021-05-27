import time
from threading import Thread
import subprocess
# KEINE UMLAUTE IN DIE DATEIEN

class Controller(object):
    def __init__(self):
        self.puzzles = []

        import Klopfraetsel
        import Puzzle1
        import SchluessekRaetsel
        import KameraRaetsel
        import RadioRaetsel
        import TasterRaetsel
        # puzlle hier Importieren und zu der Liste hinzufuegen
# die Reihenfolge hier ist auch die Reihenfolge der Puzzle!
        self.puzzles.append(Klopfraetsel.Klopfraetsel())
        self.puzzles.append(SchluessekRaetsel.SchluesselRaetsel())
        self.puzzles.append(KameraRaetsel.KameraRaetsel())
        #self.puzzles.append(TasterRaetsel.TasterRaetsel())
        self.puzzles.append(Puzzle1.Puzzle1())
        self.puzzles.append(RadioRaetsel.RadioRaetsel())
        self.hint_queue = []
        self.run_thread = Thread(target=self.run_func)

    def run_func(self):

        print("running")
        print(self.puzzles)
        self.puzzles[0].activated = True
        while len(self.puzzles) > 0:
            while not self.puzzles[0].solved:
                pass
            self.puzzles.pop(0)
            if len(self.puzzles) > 0:
                self.puzzles[0].activated = True
            print(str(len(self.puzzles)))
        print("GEWONNEN!")

    def reset_timer(self):
        pass

    def deactivate(self, puzzle):  # muss hinweis und puzzle entfernen
        self.puzzles.remove(puzzle)
        for h in puzzle.hints:
            self.hint_queue.remove(h)

    ''' Multithreading:
    def activate(self, id):
        for p in puzzles:
            if p.id == id:
                active_puzzles.append(p)
                p.activated = True
                return
                '''


class Puzzle(object):
    def __init__(self):
        self.id = None
        self.controller = "test"

        self.hints = []

        self.activated = False
        self.solved = False

        self.run_thread = Thread(target=self.run_thread_func)
        self.run_thread.start()
        self.interact_thread = Thread(target=self.interact)

    def run_thread_func(self):

        while not self.activated:
            pass
        self.init()
        self.interact_thread.start()

        timer = 0
        next_hint = 0

        while not self.solved:
            print("Not Solved" + str(timer))
            # alle fuenf Sekunden kommt ein Hinweis
            if timer == 60:
                # fur jedes Raetsel muss es zwei Hinweise geben. Nach den naechsten funf Sekunden loest sich das Raetsel von alleinr
                if next_hint == 2:
                    self.solved = True
                self.hints[next_hint].show()
                timer = 0
                next_hint = next_hint + 1
            timer = timer + 1
            time.sleep(1)
        self.deinit()

    def init(self):
        raise NotImplementedError

    def interact(self):
        raise NotImplementedError

    def deinit(self):
        raise NotImplementedError


class Hint(object):
    def __init__(self, puzzle, file):
        self.puzzle = puzzle
        self.file = file

    def show(self):
        # implemtierung von filmabspielen muss noch hinzugefuegt werden
        # argumente fuer omxplayer: -b -loop --no-osd
        # killall omxplayer, nach ende des hinweises
        subprocess.Popen("omxplayer",)
        print("showing hint "+str(self.file))


def make_hint(puzzle, file):
    return Hint(puzzle, file)


if __name__ == "__main__":
    Controller().run_thread.start()
