import beat_the_room
import RPi.GPIO as gpio
import time


class NumpadRaetsel(beat_the_room.Puzzle):

    def init(self):
        gpio.cleanup()
        
        self.zeile = [7, 8, 1, 16]
        self.spalte = [24, 6, 15, 13]
        
        self.matrix = [["1","2","3", "A"],
          ["4","5","6", "B"],
          ["7","8","9", "C"],
          ["*", "0", "#", "D"]]


        self.password = ["4", "0", "2", "8"]

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        for j in range(4):
            gpio.setup(self.spalte[j], gpio.OUT)
            gpio.output(self.spalte[j], 1)
            gpio.setup(self.zeile[j],gpio.IN,
                   pull_up_down=gpio.PUD_UP)
        print("Hi")

    def readKeypad(self):
      print("Schleife")
      while True:
          for j in range(4):
              gpio.output(self.spalte[j], 0)
              for i in range(4):
                  if gpio.input(self.zeile[i]) == 0:
                      benutzerEingabe = self.matrix[i][j]
                      #if benutzerEingabe == "*":
                       #   continue
                      print("Taste")
                      print(benutzerEingabe)
                      while gpio.input(self.zeile[i]) == 0:
                          pass
                      return benutzerEingabe
              gpio.output(self.spalte[j], 1)
      return False



    def interact(self):
        lastInputList = []
        while not self.solved:
            if lastInputList[-4:] != self.password:
                number = self.readKeypad()
                lastInputList.append(number)
                print("Hier")
                print(lastInputList)
            else:
                self.solved = True

    def deinit(self):
        pass

