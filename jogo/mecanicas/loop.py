import time
import random

from . import som
from . import mecanicas
from .inputbox import ler_texto
from .buttonbox import escolher_classe

from ..gui.tela import Tela

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.tesouro import Tesouro
from ..personagens.npc.npc import NPC
from ..personagens.pocao import Pocao
from ..personagens.inimigos.boss import Boss

import pygame

def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def executar():
    som.iniciar_musica()

    nome = ler_texto()
    classe = escolher_classe()
    match classe:
        case "Guerreiro":
            aventureiro = Guerreiro(nome)
        case "Tank":
            aventureiro = Tank(nome)
        case _:
            aventureiro = Aventureiro(nome)

    tesouro = Tesouro()
    npc = NPC(tesouro)
    pocao = Pocao([random.randint(0, 9), random.randint(0, 9)])
    tela = Tela()

    if pocao == npc or pocao == tesouro:
        pocao = Pocao([random.randint(0, 9), random.randint(0, 9)])

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False   
                    
                if teclas[pygame.K_c]:
                    aventureiro.trocar_char()
                elif teclas[pygame.K_v]:
                    aventureiro.trocar_cor()
                elif teclas[pygame.K_b]:
                    aventureiro.trocar_cor(aleatorio=True)
                elif teclas[pygame.K_n]:
                    aventureiro.aumentar_dificuldade()
                elif teclas[pygame.K_m]:  
                    aventureiro.diminuir_dificuldade()

                if teclas[pygame.K_SPACE]:
                    mecanicas.conversar(aventureiro, npc)
                    aprimoramento = npc.abrir_loja(aventureiro)
                    if aprimoramento:
                        if aprimoramento == "Arma" and aventureiro.nivel > 0:
                            aventureiro.forca += 3
                            aventureiro.nivel -= 1
                        elif aprimoramento == "Armadura" and aventureiro.nivel > 0:
                            aventureiro.defesa += 3
                            aventureiro.nivel -= 1
                    tela = Tela()
                else:
                    direcao = determinar_direcao(teclas)
                    if direcao != "" and not mecanicas.movimentar(aventureiro, direcao, npc):
                        jogo_rodando = False
                    if pocao is not None and aventureiro.posicao == pocao.posicao:
                        aventureiro.usar_pocao(pocao)
                        pocao = None
                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss(aventureiro.dificuldade)
                        if mecanicas.iniciar_combate(aventureiro, boss):
                            aventureiro.status = f"Parabéns! Você derrotou {boss.nome} e encontrou o tesouro!"
                        else:
                            aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                        jogo_rodando = False

        # Renderização na tela
        tela.renderizar(aventureiro, tesouro, npc, pocao)
        pygame.time.Clock().tick(60)

    time.sleep(2)