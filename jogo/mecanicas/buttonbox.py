from ..gui.buttonbox import ButtonBox

import pygame

def escolher_classe():
    buttonbox = ButtonBox()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return ""

            if evento.type == pygame.MOUSEBUTTONUP:
                clique = ButtonBox.mapear_clique(pygame.mouse.get_pos())
                if clique:
                    return clique

        buttonbox.renderizar()