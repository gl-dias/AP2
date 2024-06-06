import random

from .inimigo import Inimigo

class Leviathan(Inimigo):
    def __init__(self, dificuldade):
        super().__init__(dificuldade)
        self.forca = int(random.randint(20, 40) * dificuldade)
        self.vida = int(random.randint(80, 200) * dificuldade)
        self.xp = 8
        self.nome = "Leviathan"