import beat_the_room
import RPi.GPIO as gpio
import time


class NumpadRaetsel(beat_the_room.Puzzle):

    matrix = [["1","2","3", "A"],
              ["4","5","6", "B"],
          ["7","8","9", "C"],
          ["*", "0", "#", "D"]]


    zeile = [8, 25, 7, 24]
    spalte = [23, 18, 15, 14]

    password = ["4", "0", "2", "8"]

    def init(self):
        gpio.cleanup()

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        for j in range(4):
            gpio.setup(spalte[j], gpio.OUT)
            gpio.output(spalte[j], 1)
            gpio.setup(zeile[j],gpio.IN,
                   pull_up_down=gpio.PUD_UP)

    def readKeypad(self):
      while True:
          for j in range(4):
              gpio.output(spalte[j], 0)
              for i in range(4):
                  if gpio.input(zeile[i]) == 0:
                      benutzerEingabe = matrix[i][j]
                      while gpio.input(zeile[i]) == 0:
                          pass
                      return benutzerEingabe
              gpio.output(spalte[j], 1)
      return False



    def interact(self):
        lastInputList = []
        while not self.solved:
            if lastInputList[-4:] != password:
                    lastInputList.append(self.readKeypad())
                    print(lastInputList)
            else:
                self.solved = True

    def deinit(self):
        pass

