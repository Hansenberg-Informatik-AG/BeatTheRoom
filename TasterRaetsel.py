
import beat_the_room
import RPi.GPIO as GPIO
import time


class TasterRaetsel(beat_the_room.Puzzle):

    # gpios initialisieren
    def init(self):
        self.id = None

        GPIO.setmode(GPIO.BCM)

        self.id = 98  # platzhalter
        self.ports = [17, 18, 27, 22]
        for i in range(4):
            GPIO.setup(self.ports[i], GPIO.OUT)
        self.states = [False for i in range(4)]
        self.clickCounts = [0 for i in range(4)]
        self.currentPin = 0
        self.key = [3, 5, 3, 1]

        pins = ""
        for i in range(4):
            pins += str(self.ports[i])+", "
        print("init(" + pins + ")")
        # reservier alle benötigten

    def interact(self):
        schwubbeldibubbeldi = time.time()
        while not self.solved:
            pin = self.checkClicks()
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
            time.sleep(0.05)
            if time.time() > schwubbeldibubbeldi + 100:
                if input() != "":
                    self.solved = True
                    self.clickCounts = [0 for i in range(4)]
                else:
                    schwubbeldibubbeldi = time.time()

    def deinit(self):
        pins = ""
        for i in range(4):
            pins += str(self.ports[i])+", "
        print("deinitialising(" + pins + ")")
        GPIO.cleanup()

    def click(self):
        self.clickCounts[self.currentPin] += 1
        self.clickCounts[self.currentPin] = self.clickCounts[self.currentPin] % 10
        self.solved = self.isSolved()

    def isSolved(self):
        return self.clickCounts == self.key

    def checkClicks(self):
        self.printStates()
        for i in range(4):
            if not GPIO.input(self.ports[i]):
                print('!')
                if not self.states[i]:
                    self.states[i] = True
                    return i
            else:
                self.states[i] = False

        return -1

    def printStates(self):
        for i in range(4):
            print(self.clickCounts[i], end="")
            

        print()
    
