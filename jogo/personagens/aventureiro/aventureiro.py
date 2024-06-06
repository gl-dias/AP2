import os.path
import random

from ...gui.cores import CORES
from ...mecanicas import som

import pygame

class Aventureiro:
    def __init__(self, nome):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida = random.randint(100, 120)
        self.posicao = [0, 0]
        self.dificuldade = 1

        self.chars = ["@", "#", "$"]
        self.cores = [CORES.branco, CORES.vermelho, CORES.verde, CORES.azul]
        self.char = "@"
        self.cor = CORES.branco

        self.nome = nome
        self.status = "Comece a explorar"

        self.xp_por_nivel = 5
        self.xp = 0
        self.nivel = 1

    def trocar_cor(self, aleatorio=False):
        if aleatorio:
            self.cor = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        else:
            if self.cor in self.cores:
                cor = self.cores.index(self.cor) + 1
                if cor == len(self.cores):
                    cor = 0
                self.cor = self.cores[cor]
            else:
                self.cor = self.cores[0]

    def trocar_char(self):
        char = self.chars.index(self.char) + 1
        if char == len(self.chars):
            char = 0
        self.char = self.chars[char]

    def ganhar_xp(self, xp_ganho):
        self.xp += xp_ganho
        if self.xp >= self.xp_por_nivel:
            self.xp -= self.xp_por_nivel
            self.xp_por_nivel += 1
            return True
        return False

    @staticmethod
    def morrer():
        morte = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "morte.wav"))
        pygame.mixer.Sound.play(morte)

    def subir_nivel(self):
        levelup = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "levelup.wav"))
        pygame.mixer.Sound.play(levelup)
        self.nivel += 1
        self.vida += 10
        self.forca += 1
        self.defesa += 1

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "W":
                y -= 1
            case "S":
                y += 1
            case "A":
                x -= 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, nova_posicao):
        self.posicao = nova_posicao

    def atacar(self):
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def ver_atributos(self):
        print("Informações de ", self.nome, ":", sep="")
        print("Vida:", self.vida)
        print("Força:", self.forca)
        print("Defesa:", self.defesa)

    def esta_vivo(self):
        return self.vida > 0
    
    def aumentar_dificuldade(self):
        self.dificuldade *= 1.1

    def diminuir_dificuldade(self):
        self.dificuldade /= 1.1
