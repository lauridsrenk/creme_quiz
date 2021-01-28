import pygame.mixer
import time
import os


class Lautsprecher:
    def abspielen(self, sound_path):
        sound = pygame.mixer.Sound(sound_path)
        laenge = sound.get_length()
        sound.play()
        time.sleep(laenge)

    def init(self):
        pygame.mixer.init()


if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(file_path, "sounds")

    l = Lautsprecher()
    l.init()
    l.abspielen(os.path.join(sound_path,"Yoshi1.wav"))
    print("ende")