
import RPi.GPIO as gpio
import time
import beat_the_room

class RadioRaetsel(beat_the_room.Puzzle):

    def init(self):
        self.hints = [beat_the_room.make_hint(self, "test.avi"),beat_the_room.make_hint(self,"hinweis2.avi")]

        gpio.setmode(gpio.BCM)

        self.matrix = [['1','2','3','A'],
            ['4','5','6','B'],
            ['7','8','9','C'],
            ['*', '0', '#','D']]
        #im zweifel ausprobieren ob es klappt
        self.zeile = [14, 15, 18, 23]
        self.spalte = [24, 25, 8, 7]

        for j in range(4):
            gpio.setup(self.spalte[j], gpio.OUT)
            gpio.output(self.spalte[j], 1)
            gpio.setup(self.zeile[j], gpio.IN, pull_up_down=gpio.PUD_UP)


    def interact(self):
        print("interacting(42)")
        lastInputList = []
        password = ["A", "3", "B", "4"]

        while lastInputList[-4:] != password:
            lastInputList.append(self.keypad())
            print(lastInputList)

        self.solved = True
        print("Fertig(42)")

    def keypad(self):
        print("waiting for input")
        while True:
            for j in range(4):
                gpio.output(self.spalte[j], 0)
                for i in range(4):
                    if gpio.input(self.zeile[i]) == 0:
                        benutzerEingabe = self.matrix[i][j]
                        while gpio.input(self.zeile[i]) == 0:
                            pass
                        return benutzerEingabe
                gpio.output(self.spalte[j], 1)
        return False

    def deinit(self):
        print("deinitlasing(42)")
        gpio.cleanup()
