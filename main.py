from jogo.mecanicas import loop

import pygame

def iniciar():
    pygame.init()

def encerrar():
    print("Saindo do jogo")
    pygame.quit()

def main():
    iniciar()
    loop.executar()
    encerrar()

if __name__ == "__main__":
    main()

