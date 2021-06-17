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
        print("Init(15)")
        # INITIALISIERE SENSOREN / HARDWARE
        global GPIO_PIN
        
        GPIO_PIN = 20
        
        self.lastKnock = time.time() * 1000
        self.mayKnock = 0
        self.counter = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def interact(self):
        print("interacting(15)")
        try:
            GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=self.lösen, bouncetime=200)
          
        
        except Exception as e:
            print(e)
            GPIO.cleanup()
            exit(-1)

    def lösen(self, value):
        print("Übergebener Value: " + str(value))
        if self.solved == True:
            return 0
        print(self.mayKnock)
        if self.mayKnock == 1:
            print("MAY NOT KNOCK")
            self.counter = 0
            self.mayKnock = 0
            # return 0 , only if the knock should not count as "first knock" of the next try
        
        try:
            self.counter +=1
            self.lastKnock = time.time() * 1000
            print("Klopfen erkannt (" + str(self.counter) + ". Klopfen)")
            
            if self.counter >= 9:
                self.solved = True
                print("Klopfrätsel wurde gelöst")
            if (self.counter % 3) == 0 and self.solved == False:
                print("WRONG KNOCK")
                self.mayKnock = 1
                time.sleep(0.5)
                self.mayKnock = 0
           
        except KeyboardInterrupt as e:
            print("Keyboard Interrupted")
            print(e)
            GPIO.cleanup()
            exit(-1)

    def deinit(self):
        print("deinit(15)")
        # DEINITIALISIERE SENSOREN / HARDWARE
        GPIO.cleanup()
