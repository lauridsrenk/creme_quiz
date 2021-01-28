import GPIO_klassen as GPIO
import time

GPIO.start()
taster = [
    GPIO.Taster(17),
    GPIO.Taster(27),
    GPIO.Taster(22),
]
leds = [
    GPIO.LED(10),
    GPIO.LED(9),
    GPIO.LED(11),
]

try:
    while True:
        for i, t in enumerate(taster):
            if t.frage_status():
                leds[i].anmachen()
                print(i)
            else:
                leds[i].ausmachen()

        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.stop()
