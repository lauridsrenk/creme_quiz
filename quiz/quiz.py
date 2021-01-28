import random
import speaker
import sounds
import GPIO_klassen as gpio
import time

s1_pin = 17
s2_pin = 27
s3_pin = 22
led1_pin = 10
led2_pin = 9
led3_pin = 11

class Model:
    def __init__(self):
        self.fragen = sounds.fragen
        self.punkte = 0
        self.aktuelle_frage = random.choice(self.fragen)
        self.beendet = False

    def gib_frage(self):
        return self.aktuelle_frage.frage

    def gib_antworten(self):
        return self.aktuelle_frage.antworten

    def neue_frage(self):
        self.aktuelle_frage = random.choice(self.fragen)
        self.fragen.remove(self.aktuelle_frage)
        if len(self.fragen) == 0:
            self.beendet = True

    def ist_beendet(self):
        return self.beendet

    def pruefe_antwort(self,antwort):
        richtig = antwort == self.aktuelle_frage.richtig
        if richtig:
            self.punkte += 1
        else:
            self.beendet = True
        return richtig

    def gib_punkte(self):
        return self.punkte

    def gib_frage_name(self):
        return self.aktuelle_frage.name

class View:
    def __init__(self, model):
        self.model = model
        self.lautsprecher = speaker.Lautsprecher()
        self.lautsprecher.init()
        gpio.start()
        self.leds = [
            gpio.LED(led1_pin),
            gpio.LED(led2_pin),
            gpio.LED(led3_pin),
        ]
        self.tasters = [
            gpio.Taster(s1_pin),
            gpio.Taster(s2_pin),
            gpio.Taster(s3_pin),
        ]

    def stelle_frage(self):
        print(self.model.gib_frage_name())
        self.lautsprecher.abspielen(self.model.gib_frage())
        for i,s in enumerate(self.model.gib_antworten()):
            self.leds[i].anmachen()
            self.lautsprecher.abspielen(s)
            self.leds[i].ausmachen()

        antwort = -1
        while antwort == -1:
            for i, t in enumerate(self.tasters):
                if t.frage_status() == 1:
                    antwort = i
                    self.leds[antwort].anmachen()

        return antwort

    def richtig(self):
        self.lautsprecher.abspielen(sounds.punktestand[self.model.gib_punkte()])
        for l in self.leds:
            l.ausmachen()

    def falsch(self):
        if(self.model.gib_punkte() == 0):
            self.lautsprecher.abspielen(sounds.falsch[0])
        else:
            self.lautsprecher.abspielen(random.choice(sounds.falsch[1:]))
    
    def start(self):
        print("start")
        #return True
        for l in self.leds:
            l.anmachen()
        self.lautsprecher.abspielen(sounds.intro)
        for l in self.leds:
            l.anmachen()
            time.sleep(0.1)
            l.ausmachen()
        self.lautsprecher.abspielen(sounds.regeln)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)

    def main(self):
        self.view.start()
        while not self.model.ist_beendet():
            self.model.neue_frage()
            antwort = self.view.stelle_frage()
            richtig = self.model.pruefe_antwort(antwort)
            if richtig:
                self.view.richtig()
            else:
                self.view.falsch()

if __name__ == "__main__":
    try:
        spiel = Controller()
        spiel.main()
        gpio.stop()
    
    except KeyboardInterrupt:
        print("stop")
        gpio.stop()
