from .aventureiro import Aventureiro

import random

class Guerreiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = random.randint(15, 30)
        self.defesa = random.randint(8, 15)
        self.vida = random.randint(90, 110)

        self.char = "G"
        self.chars.append("G")

    def atacar(self):
        return self.forca + random.randint(1, 8)