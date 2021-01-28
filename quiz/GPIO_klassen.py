import RPi.GPIO as GPIO
import time

def start():
    GPIO.setmode(GPIO.BCM)

def stop():
    GPIO.cleanup()

def default_callback(pin):
    pass

class LED:
    def __init__(self,pin):
        self.pin = pin
        self.an = False
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin,False)
    def anmachen(self):
        self.an = True
        GPIO.output(self.pin,True)
    def ausmachen(self):
        self.an = False
        GPIO.output(self.pin,False)
    def ist_an(self):
        return self.an

class Callback_Taster:
    def __init__(self,pin,callback=default_callback):
        self.pin = pin
        self.callback = callback
        GPIO.setup(self.pin,GPIO.IN)
        GPIO.add_event_detect(
            self.pin,
            GPIO.RISING,
            callback=self.callback,
            bouncetime=200
        )
    def aendere_callback(self,callback):
        GPIO.remove_event_detect(self.pin)
        self.callback = callback
        GPIO.add_event_detect(
            self.pin,
            GPIO.RISING,
            callback=self.callback,
            bouncetime=200
        )

class Taster:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def frage_status(self):
        return GPIO.input(self.pin)

class BlinkLED(LED):
    def blink(self,an,aus=-1):
        self.anmachen()
        time.sleep(an)
        self.ausmachen()
        if aus >= 0:
            time.sleep(aus)
        else:
            time.sleep(an)
        

if __name__ == "__main__":
    start()
        
    s1 = Taster(11)

    try:
        while True:
            aktiv = s1.frage_status()
            print(aktiv)
            time.sleep(0.1)
    except KeyboardInterrupt:
        stop()
