from beat_the_room import Puzzle
import RPi.GPIO as GPIO
import time

class KameraRaetsel(Puzzle):
    def init(self):
        print('init')
        self.id = 1
       

        GPIO.setmode(GPIO.BOARD)

        self.pin_to_circuit = 7
        GPIO.setup(pin_to_circuit, GPIO.IN)


#währenddessen soll livecam mitlaufen

    def interact(self):
        count = 0
        while count < 20:
            if True: #bin ich dunkel? TODO
                count+=1
            else:
                count = 1
            time.sleep(0.1)
        self.solved=True

    def deinit(self):
        GPIO.cleanup()
        #Port speziefizieren???
    
