import random

from .inimigo import Inimigo

class Ogro(Inimigo):
    def __init__(self, dificuldade):
        super().__init__(dificuldade)
        self.forca = int(random.randint(10, 25) * dificuldade)
        self.vida = int(random.randint(50, 100) * dificuldade)
        self.xp = 3
        self.nome = "Ogro"