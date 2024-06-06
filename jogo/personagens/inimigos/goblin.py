import random

from .inimigo import Inimigo

class Goblin(Inimigo):
    def __init__(self, dificuldade):
        super().__init__(dificuldade)
        self.forca = int(random.randint(5, 15) * dificuldade)
        self.vida = int(random.randint(10, 40) * dificuldade)
        self.xp = 1
        self.nome = "Goblin"