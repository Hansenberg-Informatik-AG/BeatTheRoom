import time
import beat_the_room
import RPi.GPIO as GPIO


class Klopfraetsel(beat_the_room.Puzzle):

    def init(self):
        GPIO.cleanup()
        # hinweis filmdatei
        # die Rätsel sind linear
        self.hints = [beat_the_room.make_hint(
            self, "test.avi"), beat_the_room.make_hint(self, "hinweis2.avi")]
        print("Init(16)")
        # INITIALISIERE SENSOREN / HARDWARE
        global GPIO_PIN
        
        GPIO_PIN = 20
        
        self.lastKnock = 0
        self.counter = 0
        self.anfang = 0
        self.fehler = True
        self.fehlerTime = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)
        
        self.anfang = time.time()

    def interact(self):
        print("interacting(15)")

        try:
            GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=self.lösen, bouncetime=175)
          
        except Exception as e:
            print(e)
            GPIO.cleanup()
            exit(-1)
    def fehler(self, message):
        print("---> Es kam zu einem unerwartetem Fehler <---")
        print("Fehlermeldung: " + message)
        self.fehler = True
        self.fehlerTime = time.time()
        self.counter = 0
        
    def lösen(self, value):
        if self.solved == True:
            return 0
        
        print (self.anfang)
        
        print ("Counter:   " + str(self.counter))
        print ("Time:      " + str(time.time() - self.anfang))
        print ("lastKnock: " + str(time.time() - self.lastKnock))
        
        #print("----" + time.time() - self.lastKnock + "----")
        if (self.fehler and time.time()-self.fehlerTime < 0.3):
            return 0
        
        if (time.time() - self.lastKnock < 0.1):
            print("-----to short on previous knock-----")
            return 0
        
        if (time.time() - self.lastKnock < 0.3 and self.counter % 3 == 0 and self.counter != 0):
            self.fehler("kein Klopfen")
            return 0 # only if the knock should not count as "first knock" of the next try
        
        if (time.time() - self.lastKnock > 2 and self.counter % 3 != 0 and self.counter != 0):
            self.fehler("zu lange gewartet")
            return 0 # only if the knock should not count as "first knock" of the next try
        
        self.lastKnock = time.time()
        self.fehler = False
        self.fehlerTime = 0
        
        try:
            self.counter +=1
            print("Klopfen erkannt (" + str(self.counter) + ". Klopfen)")
            
            if self.counter >= 9:
                self.solved = True
                print("Klopfrätsel wurde gelöst")
           
        except KeyboardInterrupt as e:
            print("Keyboard Interrupted")
            print(e)
            GPIO.cleanup()
            exit(-1)

    def deinit(self):
        print("deinit(15)")
        # DEINITIALISIERE SENSOREN / HARDWARE
        GPIO.cleanup()
