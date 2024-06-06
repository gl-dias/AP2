from .aventureiro import Aventureiro

import random

class Tank(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = random.randint(8, 15)
        self.defesa = random.randint(15, 25)
        self.vida = random.randint(120, 150)

        self.char = "T"
        self.chars.append("T")

    def defender(self, dano):
        dano_levado = dano - self.defesa - random.randint(1, 4)
        if dano_levado > 0:
            self.vida -= dano_levado