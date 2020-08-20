from beat_the_room import Puzzle
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from PIL import Image


class KameraRaetsel(Puzzle):
    def init(self):
        print('init')
        self.id = 1

        global camera
        camera = PiCamera()
        # GPIO.setmode(GPIO.BOARD)

        #self.pin_to_circuit = 7
        #GPIO.setup(pin_to_circuit, GPIO.IN)


# währenddessen soll livecam mitlaufen


    def interact(self):
        dark = False
        camera.start_preview()
        count = 0
        while count < 60:
            if dark:  # bin ich dunkel? TODO

                count += 1
            else:
                camera.capture('/home/pi/Desktop/image%s.jpg' % count)
                i = Image.open('/home/pi/Desktop/image%s.jpg' % count)
                pix = i.load()
                width, height = i.size
                cnt = 0
                for x in range(width):
                    for y in range(height):
                        cnt += 1
                        print(pix[x, y])
                count = 1
            time.sleep(5)
        self.solved = True

    def deinit(self):
        camera.stop_preview()
        # Port speziefizieren???
