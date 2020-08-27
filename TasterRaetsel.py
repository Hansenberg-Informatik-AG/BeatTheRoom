
import RPi.GPIO as GPIO


class TasterRaetsel(beat_the_room.Puzzle):

    #gpios initialisieren
    def init(self):
        GPIO.setmode(GPIO.BCM)
        self.ports = [17,18,27,22]
        self.states = [False for i in range(4)]
        self.clickCounts = [0 for i in range(4)]
        self.currentPin = 0
        #reservier mal paar pins

    def interact(self):
        while not self.solved:
            pin = checkClicks()
            if pin != -1:
                if pin == self.currentPin:
                    self.clickCounts[pin] += 1
                elif if pin == self.currentPin + 1:
                    self.currentPin += 1
                    self.clickCounts[self.currentPin]

    def deinit(self):
        pass


    def checkClicks(self):
        for i in range(4):
            if GPIO.input(self.ports[i]):
                if not self.states[i]:
                    self.state[i] = True
                    return i
            else:
                self.states[i] = False
                
                
        return -1
