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
        while self.rc_time>10:      
            pass 
        self.solved=true
        
    def rc_time(self):
        count = 0

        while (GPIO.input(self.pin_to_circuit) == GPIO.LOW):
            time.sleep(0.1)
            count += 1

        return count

    def deinit(self):
        GPIO.cleanup()
        #Port speziefizieren???
    