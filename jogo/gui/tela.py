from .cores import CORES
from ..personagens.tesouro import Tesouro
from ..personagens.pocao import Pocao
from ..personagens.aventureiro.aventureiro import Aventureiro

import pygame

GRID = 40
MARGEM = 10
LARGURA = GRID * 10 + 450
ALTURA = GRID * 10 + 100
FONTE = "Courier New"

def centralizar_texto(texto, posicao_original):
    x = GRID * posicao_original[0] + (LARGURA - 10 * GRID) // 2 + (GRID - texto.get_width()) // 2
    y = GRID * posicao_original[1] + (ALTURA - 10 * GRID) // 2 + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

        self.fonte_gde = pygame.font.SysFont(FONTE, GRID)
        self.fonte_peq = pygame.font.SysFont(FONTE, GRID // 2)

    def dificuldade(self, dificuldade_do_jogo):
        dif = f"{dificuldade_do_jogo:.4f}"
        texto = self.fonte_peq.render(dif, True, CORES.branco)
        self.display.blit(texto, [LARGURA - texto.get_width() - MARGEM, MARGEM])

    def renderizar(self, aventureiro, tesouro, npc, pocao):
        self.display.fill(CORES.preto)
        self.informacoes(aventureiro)
        self.dificuldade(aventureiro.dificuldade)
        self.personagem(tesouro)
        self.personagem(aventureiro)
        self.personagem(npc)
        if pocao is not None:
            self.personagem(pocao)
        self.mapa(aventureiro, tesouro, npc, pocao)
        pygame.display.update()

    def mapa(self, aventureiro, tesouro, npc, pocao):
        texto = self.fonte_gde.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                posicoes = [aventureiro.posicao, tesouro.posicao, npc.posicao]
                if pocao is not None:
                    posicoes.append(pocao.posicao)
                if [linha, coluna] not in posicoes:
                    self.display.blit(texto, centralizar_texto(texto, [linha, coluna]))

    def personagem(self, personagem):
        if isinstance(personagem, Tesouro):
            cor = CORES.vermelho
        elif isinstance(personagem, Pocao):
            cor = CORES.azul
        elif isinstance(personagem, Aventureiro):
            cor = personagem.cor
        else:
            cor = CORES.branco 

        texto = self.fonte_gde.render(personagem.char, True, cor)
        self.display.blit(
        texto,
        centralizar_texto(texto, [personagem.posicao[0], personagem.posicao[1]])
    )

    def informacoes(self, aventureiro):
        atributos = f"{aventureiro.nome} nv. {aventureiro.nivel} ({aventureiro.xp} / {aventureiro.xp_por_nivel}) - " \
            f"Vida: {aventureiro.vida} / Força: {aventureiro.forca} / Defesa: {aventureiro.defesa}"
        texto = self.fonte_peq.render(atributos, True, CORES.branco)
        
        x_centralizado = LARGURA // 2 - texto.get_width() // 2
        self.display.blit(texto, [x_centralizado, ALTURA - MARGEM - texto.get_height()])

        texto = self.fonte_peq.render(aventureiro.status, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    