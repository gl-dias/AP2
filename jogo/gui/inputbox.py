from .cores import CORES

import pygame

L = 400
M = 10
A_F = 20
L_R = L - 2 * M
A_R = A_F + 2 * M
FONTE = "Courier New"

class InputBox:
    def __init__(self):
        self.display = pygame.display.set_mode((L, 2 * A_F + 5 * M))
        pygame.display.set_caption("Rogue")

        self.fonte = pygame.font.SysFont(FONTE, A_F)

    def renderizar(self, resposta):
        self.display.fill(CORES.preto)

        texto = self.fonte.render("Informe o seu nome:", True, CORES.branco)
        self.display.blit(texto, [M, M])

        texto = self.fonte.render(resposta, True, CORES.branco)
        self.display.blit(texto, [2 * M, 3 * M + A_F])

        rect = pygame.Rect(M, 2 * M + A_F, L_R, A_R)
        pygame.draw.rect(self.display, CORES.branco, rect, 3)

        pygame.display.update()