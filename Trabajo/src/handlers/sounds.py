import os
import pygame


def play_sound(sound):
    pygame.init()
    pygame.mixer.init()
    archivo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sounds", sound))
    s = pygame.mixer.Sound(archivo)
    pygame.mixer.Sound.play(s)
