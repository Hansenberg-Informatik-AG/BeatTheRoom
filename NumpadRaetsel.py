import beat_the_room
import RPi.GPIO as gpio
import time

class NumpadRaetsel(beat_the_room.Puzzle):
    def init(self):
        print("Init Numpad")
        gpio.cleanup()
        
        self.zeile = [16, 7, 8, 12]
        self.spalte = [24, 6, 5, 13]

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        
        for j in range(4):
            gpio.setup(self.spalte[j], gpio.OUT)
            gpio.setup(self.zeile[j],gpio.IN,
                   pull_up_down=gpio.PUD_UP)
        
        # Keypad
        self.matrix = [
            [1,2,3,"A"],
            [4,5,6,"B"],
            [7,8,9,"C"],
            ["*",0,"#","D"]
        ]

        self.password = ["4", "0", "2", "8"]
        print("End init Numpad")

    def readKeypad(self):
      print("Schleife")
      while True:
          for j in range(4):
              gpio.output(self.spalte[j], gpio.HIGH)
              for i in range(4):
                  if gpio.input(self.zeile[i]) == 1:
                      benutzerEingabe = self.matrix[i][j]
                      print("Taste")
                      print(benutzerEingabe)
                      while gpio.input(self.zeile[i]) == 0:
                          pass
                      return benutzerEingabe
              gpio.output(self.spalte[j], gpio.LOW)
      return False

    def interact(self):
        lastInputList = []
        while not self.solved:
            time.sleep(0.2)
            
            if lastInputList[-4:] != self.password:
                number = self.readKeypad()
                lastInputList.append(number)
                print("Hier")
                print(lastInputList)
            
            else:
                self.solved = True

    def deinit(self):
        pass
