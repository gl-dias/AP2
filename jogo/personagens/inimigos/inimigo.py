import os.path
import random

from ...mecanicas import som

import pygame

class Inimigo:
    def __init__(self, dificuldade):
        self.forca = random.randint(5, 25)
        self.vida = random.randint(10, 100)
        self.xp = 1

    @staticmethod
    def morrer():
        barulho = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "monstro.mp3"))
        pygame.mixer.Sound.play(barulho)

    def atacar(self):
        return self.forca

    def defender(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0
    
    
    