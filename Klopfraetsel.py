import time
import beat_the_room
import RPi.GPIO as GPIO


class Klopfraetsel(beat_the_room.Puzzle):

    def init(self):
        GPIO.cleanup()
        # Annika und Johann Versuch zum Klopfrätsel
        # Sollte einmaliges Klopfen erkennen
        # hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(
            self, "test.avi"), beat_the_room.make_hint(self, "hinweis2.avi")]
        # print("Init(15)")
        # INITIALISIERE SENSOREN / HARDWARE
        global GPIO_PIN
        GPIO_PIN = 15
        self.counter = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def interact(self):
        print("interacting(15)")
        try:
            GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING,
                              callback=self.lösen, bouncetime=100)
        # time.sleep(10)
        # sobald diese variable gesetzt ist, ist das Rätsel fertig! Hier muss wahrscheinlich immer eine while Schleife rein!
           # while self.solved == False:
           #     time.sleep(0.001)

        
        except Exception as e:
            print(e)
            GPIO.cleanup()
            exit(-1)

    def lösen(self, null):
        if self.solved == True:
                pass
        try:
            print("Klopfen")
            self.counter +=1
            if self.counter >= 9:
                self.solved = True
                self.deinit()
                print("Fertig(15)")
            if self.counter%3==0 and self.solved == False:
                time.sleep(0.5)
            print(self.counter)
           
        except KeyboardInterrupt as e:
            print(e)
            GPIO.cleanup()
            exit(-1)

    def deinit(self):
        print("deinitlasing(15)")
        # DEINITIALISIERE SENSOREN / HARDWARE
        GPIO.cleanup()
