import sys
import time

#Função achada no StackOverflow para printar a linha lentamente.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
