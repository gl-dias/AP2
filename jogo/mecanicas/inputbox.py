from ..gui.inputbox import InputBox

import pygame

def ler_texto():
    inputbox = InputBox()

    texto = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return texto

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RETURN:
                    return texto
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif len(texto) < 25:
                    texto += evento.unicode

        inputbox.renderizar(texto)