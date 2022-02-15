from beat_the_room import Puzzle
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from PIL import Image
import vlc

class KameraRaetsel(Puzzle):
    def init(self):
        print('init')
        self.id = 1

        global camera
        camera = PiCamera()
        camera.start_preview()
        # GPIO.setmode(GPIO.BOARD)

        #self.pin_to_circuit = 7
        #GPIO.setup(pin_to_circuit, GPIO.IN)


# währenddessen soll livecam mitlaufen

    def interact(self):
        dark = False
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
                print(str(brightTotal/cnt)+" Average")
                #Hier den Grenzwert der Kamera verändern
                self.solved = (brightTotal/cnt) < 50
                count = 1
            time.sleep(5)
        self.solved = True

    def deinit(self):
        camera.stop_preview()
        # Port speziefizieren???
        p = vlc.MediaPlayer("BeatTheRoom/Audio_und_Videodateien/3.Kamera-Deaktiviert.mp3")
        p.play()
