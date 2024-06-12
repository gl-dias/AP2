from ..personagens.npc.buttonboxnpc import ButtonBoxNpc

import pygame

def escolher_aprimoramento():
    buttonboxnpc = ButtonBoxNpc()

        # Loop até o jogador fazer uma escolha ou fechar a loja
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return ""

            if evento.type == pygame.MOUSEBUTTONUP:
                clique = ButtonBoxNpc.mapear_clique(pygame.mouse.get_pos())
                if clique:
                    return clique

        buttonboxnpc.renderizar()