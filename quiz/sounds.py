import os

file_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(file_path, "sounds")

class Frage:
    def __init__(self, frage, ra):
        self.frage = os.path.join(sound_path, "fragen", frage, "f.wav")
        self.antworten = [
            os.path.join(sound_path, "fragen", frage, "a1.wav"),
            os.path.join(sound_path, "fragen", frage, "a2.wav"),
            os.path.join(sound_path, "fragen", frage, "a3.wav")
        ]
        self.richtig = ra
        self.name = frage

intro = os.path.join(sound_path,"Intro.wav")
regeln = os.path.join(sound_path,"Regeln.wav")
falsch = [
    os.path.join(sound_path, "falsch", "KindaCringe.wav"),
    os.path.join(sound_path, "falsch", "KeinerSoDumm.wav"),
    os.path.join(sound_path, "falsch", "Nicht Richtig.wav"),
    os.path.join(sound_path, "falsch", "Nicht Richtig, Nochmal.wav"),
]
richtig = [
    os.path.join(sound_path, "richtig", "Richtig.wav"),
    os.path.join(sound_path, "richtig", "Richtig 2.wav"),
    os.path.join(sound_path, "richtig", "Richtig 3.wav"),
]
fragen = [
    #Frage("yoshi",0),
    Frage("durchmesser",0),
    Frage("camember",1),
    Frage("shitass",0),
    Frage("pferd",2),
    Frage("quote",1),
    Frage("obama",1)
]
punktestand = [
    None,
    os.path.join(sound_path,"punktestand","1 Punkt.wav"),
    os.path.join(sound_path,"punktestand","2 Punkte.wav"),
    os.path.join(sound_path,"punktestand","3 Punkte.wav"),
    os.path.join(sound_path,"punktestand","4 Punkte.wav"),
    os.path.join(sound_path,"punktestand","5 Punkte.wav"),
    os.path.join(sound_path,"punktestand","6 Punkte.wav"),
    os.path.join(sound_path,"punktestand","7 Punkte.wav"),
]
