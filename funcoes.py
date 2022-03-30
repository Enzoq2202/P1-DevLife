import sys
import time
from random import *

#Função achada no StackOverflow para printar a linha lentamente.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.015)
#Função sorteio dos dados
def sorteio_dado1():
    dado1 = randint(1,3)
    return dado1
def sorteio_dado2():
    dado2 = randint(1,3)
    return dado2

#Função que vai percorrer a lista e definir os tesouros
def sorteio_tesouros(posicao):
    if posicao <= 8:
        valor = randint(0,3)
    elif posicao > 8 and posicao < 17:
        valor = randint(4,7)
    elif posicao > 16 and posicao < 25:
        valor = randint(8,11)
    else:
        valor = randint(12,15)
    return valor

#Função que demonstra a posição do jogador no print
def posicao_lista(lista,posicao,personagem):
    lista_retorno = []
    if posicao > 32:
        for elem in lista:
            lista_retorno.append(elem)
        lista_retorno[31] = personagem
        print('Não é possível mais avançar, você se encontra na posição de número 32. Redirecionando personagem.')
        return 'Redirecionando o personagem.'
    else:
        for elem in lista:
            lista_retorno.append(elem)
        lista_retorno[posicao-1] = personagem
        return lista_retorno

#Função que faz a trajetória de volta do jogador
def retorne_posicao(lista,posicao,personagem):
    lista_retorno = []
    for elem in lista:
        lista_retorno.append(elem)
    lista_retorno[posicao-1] = personagem
    return lista_retorno
