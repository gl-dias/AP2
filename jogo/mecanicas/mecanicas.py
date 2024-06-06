import random

from . import som

from ..personagens.inimigos.leviathan import Leviathan
from ..personagens.inimigos.goblin import Goblin
from ..personagens.inimigos.ogro import Ogro

# Combate
def iniciar_combate(aventureiro, inimigo):
    while True:
        dano = aventureiro.atacar()
        inimigo.defender(dano)
        if not inimigo.esta_vivo():
            if aventureiro.ganhar_xp(inimigo.xp):
                aventureiro.subir_nivel()
            else:
                inimigo.morrer()
            return True

        dano = inimigo.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            aventureiro.morrer()
            return False

def existe_obstaculo(posicao, npc):
    x, y = posicao
    if x < 0 or x > 9 or y < 0 or y > 9:
        return True

    if posicao == npc.posicao:
        return True

    return False

# Operação principal do jogo
def movimentar(aventureiro, direcao, npc):
    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if existe_obstaculo(pos_futura, npc):
        return True

    aventureiro.andar(pos_futura)

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = random.choices([Leviathan, Ogro, Goblin], [1, 3, 10])[0](aventureiro.dificuldade)
        if iniciar_combate(aventureiro, monstro):
            aventureiro.status = f"{monstro.nome} foi derrotado!"
            return True

        aventureiro.status = f"Você foi derrotado por {monstro.nome}! Game Over..."
        return False

    aventureiro.status = "Continue explorando"
    som.passo()
    return True

def conversar(aventureiro, npc):
    x_a, y_a = aventureiro.posicao
    x_n, y_n = npc.posicao

    if (x_a + 1 == x_n or x_a - 1 == x_n) and y_a == y_n:
        aventureiro.status = npc.mensagem
        npc.falar()

    if (y_a + 1 == y_n or y_a - 1 == y_n) and x_a == x_n:
        aventureiro.status = npc.mensagem
        npc.falar()

