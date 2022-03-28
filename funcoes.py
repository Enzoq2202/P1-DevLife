import sys
import time
from random import *

#Função achada no StackOverflow para printar a linha lentamente.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
#Função sorteio dos dados
def sorteio_dado1():
    dado1 = randint(1,3)
    return dado1
def sorteio_dado2():
    dado2 = randint(1,3)
    return dado2

#Função que vai percorrer a lista e definir os tesouros
def sorteio_tesouros(lista,dados):
    num_sorteado = lista[dados-1][0]
    if num_sorteado <= 8:
        valor = randint(1,3)
    elif num_sorteado > 8 and num_sorteado < 17:
        valor = randint(4,7)
    elif num_sorteado > 16 and num_sorteado < 25:
        valor = randint(8,11)
    else:
        valor = randint(12,15)
    return valor

#Função que demonstra a posição do jogador no print
def posicao_lista(lista,posicao,personagem):
    lista[posicao-1] = personagem
    return lista
