import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
GPIO.setwarnings(False)
 
RELAIS_1_GPIO = 17

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus

time.sleep(1)

#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an

#GPIO.cleanup()