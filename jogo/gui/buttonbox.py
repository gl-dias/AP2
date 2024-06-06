from .cores import CORES

import pygame

M = 10
A_T = 20
L_B = 150
A_B = 40
L = 2 * L_B + 3 * M
A = 3 * M + A_T + A_B
FONTE = "Courier New"

class ButtonBox:
    def __init__(self):
        self.display = pygame.display.set_mode((L, A))
        pygame.display.set_caption("Rogue")

        self.fonte = pygame.font.SysFont(FONTE, A_T)

    # método estático
    @staticmethod # -> decorator
    def mapear_clique(pos):
        x, y = pos

        if M <= x <= M + L_B and 2 * M + A_T <= y <= 2 * M + A_T + A_B:
            return "Guerreiro"

        if 2 * M + L_B <= x <= 2 * M + 2 * L_B and 2 * M + A_T <= y <= 2 * M + A_T + A_B:
            return "Tank"

        return ""

    def renderizar(self):
        self.display.fill(CORES.preto)

        texto = self.fonte.render("Agora, escolha sua classe:", True, CORES.branco)
        self.display.blit(texto, [M, M])

        rect = pygame.Rect(M, 2 * M + A_T, L_B, A_B)
        pygame.draw.rect(self.display, CORES.branco, rect)

        rect = pygame.Rect(2 * M + L_B, 2 * M + A_T, L_B, A_B)
        pygame.draw.rect(self.display, CORES.branco, rect)

        texto = self.fonte.render("Guerreiro", True, CORES.preto)
        x = M + (L_B - texto.get_width()) // 2
        y = 2 * M + A_T + (A_B - texto.get_height()) // 2
        self.display.blit(texto, [x, y])

        texto = self.fonte.render("Tank", True, CORES.preto)
        x = 2 * M + L_B + (L_B - texto.get_width()) // 2
        self.display.blit(texto, [x, y])

        pygame.display.update()