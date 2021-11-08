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
                   pull_up_down=gpio.PUD_DOWN)
        
        # Keypad
        self.matrix = [
            [1,4,7,"*"],
            [2,5,8,0],
            [3,6,9,"#"],
            ["A","B","C","D"]
        ]

        self.password = ["4", "0", "2", "8"]
        print("End init Numpad")

    def readKeypad(self, line, characters):
      print("Schleife")
      while True:
          gpio.output(self.spalte[line], gpio.HIGH)
          
          char = -1
          benutzerEingabe = -1
                
          if gpio.input(self.zeile[0]) == 1:
              char = 0
              benutzerEingabe = characters[0]
            
          if gpio.input(self.zeile[1]) == 1:
              char = 1
              benutzerEingabe = characters[1]
            
          if gpio.input(self.zeile[2]) == 1:
              char = 2
              benutzerEingabe = characters[2]
            
          if gpio.input(self.zeile[3]) == 1:
              char = 3
              benutzerEingabe = characters[3]
              
          if (char != -1):
              while gpio.input(self.zeile[char]) == 0:
                  pass
            
              print("Taste")
              print(benutzerEingabe)
              gpio.output(self.spalte[line], gpio.LOW)
          
              return benutzerEingabe
          else: 
              gpio.output(self.spalte[line], gpio.LOW)
          
      return False

    def interact(self):
        lastInputList = []
        while not self.solved:
            time.sleep(0.2)
            
            if lastInputList[-4:] != self.password:
                for i in range(4):
                    number = self.readKeypad(i, self.matrix[i])
                
                    lastInputList.append(number)
                    print("Hier")
                    print(lastInputList)
            
            else:
                self.solved = True

    def deinit(self):
        pass
