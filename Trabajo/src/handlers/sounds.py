import os
import pygame


def play_sound(sound):
    pygame.init()
    pygame.mixer.init()
    archivo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sounds", sound))
    s = pygame.mixer.Sound(archivo)
    if sound == "game music.wav":
        pygame.mixer.Sound.play(s, -1)
    else:
        pygame.mixer.Sound.play(s)
