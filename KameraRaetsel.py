from beat_the_room import Puzzle
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from PIL import Image

# Puzzle: 
# Make camera dark (hold hand right in front of it)
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
        while not self.solved:
            if dark:  # bin ich dunkel? TODO

                count += 1
            else:
                camera.capture('/home/pi/Desktop/image%s.jpg' % count)
                i = Image.open('/home/pi/Desktop/image%s.jpg' % count)
                pix = i.load()
                width, height = i.size
                # Anzahl der Pixel
                cnt = 0
                # Summe der Helligkeiten der Pixel um die Helligkeit rauszufinden
                brightTotal = 0
                for x in range(0, width, 16):
                    for y in range(0, height, 16):
                        cnt += 1
                        rgb = pix[x, y]
                        R = rgb[0]
                        G = rgb[1]
                        B = rgb[2]
                        Y = 0.375 * R + 0.5 * G + 0.125 * B
                        brightTotal += Y
                print(str(brightTotal/cnt)+"Average")
                self.solved = (brightTotal/cnt) < 35
                count = 1
            time.sleep(5)
        self.solved = True

    def deinit(self):
        camera.stop_preview()
        # Port speziefizieren???
