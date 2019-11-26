import time
from threading import Thread

class Controller(object):
    def __init__(self):
        self.puzzles = []
        self.active_puzzles = []

        self.hint_queue = []

    def run():
        pass

    def reset_timer(self):
        pass

    def deactivate(self, puzzle): # muss hinweis und puzzle entfernen
        pass

    def activate(self, id):
        pass

class Puzzle(object):
    def __init__(self, controller):
        self.id = None
        self.controller = controller

        self.hints = []

        self.activates_ids = []

        self.activated = False
        self.solved = False

        self.run_thread = Thread(target=self.run_thread_func)
        self.run_thread.start()

        self.interact_thread = Thread(target=self.interact)

    def run_thread_func(self):
        self.init()

        while not self.activated:
            pass

        self.controller.active_puzzles.append(self)
        self.interact_thread.start()

        while not self.solved:
            pass

        self.controller.reset_timer()
        self.controller.deactivate(sel)
        for id in activates_ids:
            self.controller.activate(id)

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
