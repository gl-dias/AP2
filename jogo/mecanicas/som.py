import os
import os.path

import pygame

DIRETORIO = os.path.join(os.getcwd(), "assets", "sound")

pygame.mixer.init()

def iniciar_musica():
    pygame.mixer.music.load(os.path.join(DIRETORIO, "song18.mp3"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

def passo():
    som = pygame.mixer.Sound(os.path.join(DIRETORIO, "andar.flac"))
    pygame.mixer.Sound.play(som)

def vitoria():
    som = pygame.mixer.Sound(os.path.join(DIRETORIO, "vitoria.wav"))
    pygame.mixer.Sound.play(som)

print(DIRETORIO)