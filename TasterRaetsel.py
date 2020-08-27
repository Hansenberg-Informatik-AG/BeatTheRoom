
from beat_the_room import Puzzle
import RPi.GPIO as GPIO


class TasterRaetsel(beat_the_room.Puzzle):

    #gpios initialisieren
    def init(self):
        GPIO.setmode(GPIO.BCM)
        self.ports = [17,18,27,22]
        self.states = [False for i in range(4)]
        self.clickCounts = [0 for i in range(4)]
        self.currentPin = 0
        self.key = [3,5,3,1]
        #reservier mal paar pins

    def interact(self):
        while not self.solved:
            pin = checkClicks()
            if pin != -1:
                if pin == self.currentPin:
                    self.click()
                elif pin == self.currentPin + 1:
                    self.currentPin += 1
                    self.click()
                elif pin == 0:
                    self.currentPin = 0
                    self.clickCounts = [0 for i in range(4)]
                    self.click()

    def deinit(self):
        pass

    def click(self):
        self.clickCounts[self.currentPin] += 1
        self.solved = self.isSolved()

    def isSolved(self):
        return self.clickCounts == self.key

    def checkClicks(self):
        for i in range(4):
            if GPIO.input(self.ports[i]):
                if not self.states[i]:
                    self.state[i] = True
                    return i
            else:
                self.states[i] = False
                
                
        return -1
