import random
from ..gui.cores import CORES

class Tesouro:
    def __init__(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0):
                break

        self.posicao = [x, y]
        self.char = "X"
        self.cor = CORES.vermelho