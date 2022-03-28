import sys
import time
from random import *

#Função achada no StackOverflow para printar a linha lentamente.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
#Função sorteio
def sorteio_dados():
    dado1 = randint(1,3)
    print(f'o primeiro dado caiu no número {dado1}.')
    dado2 = randint(1,3)
    print(f'o segundo dado caiu no número {dado2}.')
    soma = dado1+dado2
    return f'A soma deles corresponde a {soma}' 

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
