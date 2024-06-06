import os.path
import random

from ...mecanicas import som
from .inimigo import Inimigo

import pygame

class Boss(Inimigo):
    def __init__(self, dificuldade):
        super().__init__(dificuldade)
        self.forca = int(random.randint(15, 30) * dificuldade)
        self.vida = int(random.randint(50, 130) * dificuldade)
        self.defesa = int(random.randint(1, 6) * dificuldade)
        self.nome = "Boss"
        self.xp = 0
    

    @staticmethod
    def morrer():
        barulho = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "vitoria.wav"))
        pygame.mixer.Sound.play(barulho)

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano

    