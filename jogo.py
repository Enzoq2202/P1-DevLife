from funcoes import *
from random import *
from colorama import Fore,Style
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from tqdm import tqdm
from time import *

#Tela inicial do jogo
print_slow(Fore.BLUE + '-----------------------------------------------------')
print()
print_slow(Fore.BLUE + '     Seja bem-vindo ao jogo Aventura em alto mar!')
print()
print_slow(Fore.BLUE + '-----------------------------------------------------')             
print()                                                                           

#Pergunta do tutorial
while True:
    pergunta_tutorial = input('Gostaria de ler a descrição do jogo? [S]/[N]: ').upper()
    if pergunta_tutorial == 'S':
        print_slow('Escolha um mergulhador profundo do mar, role os dados e mergulhe no oceano')
        print()
        print_slow('Adquira sua fortuna: pouse em um pedaço de tesouro para adicioná-lo à sua coleção. Quanto mais fundo você for, mais valioso pode ser seu tesouro.')
        print()
        print_slow('Não fique muito pegajoso: todos os mergulhadores têm um suprimento compartilhado de oxigênio. Então, se você passar muito tempo procurando tesouros, você pode ficar preso lá de vez.')
        print()
        break
    elif pergunta_tutorial == 'N':
        print('Carregando jogo........')
        print(Fore.WHITE)
        #Cria barra em porcentagem
        for e in tqdm([1,2,3,4,5,6,7,8,9]):
            sleep(0.5)
        print(Style.RESET_ALL)
        print(Fore.BLUE)
        break
    else:
        print(Fore.RED + 'Entrada Inválida')
        print(Style.RESET_ALL)
        print(Fore.BLUE)
#Criando Variáveis
oxigenio = 25
tesouros_jogador1 = []
tesouros_jogador2 = []
lista_posicao_tesouros = [
    [1],[2],[3],[4],[5],[6],[7],[8],
    [9],[10],[11],[12],[13],[14],[15],[16],
    [17],[18],[19],[20],[21],[22],[23],[24],
    [25],[26],[27],[28],[29],[30],[31],[32]
]
#Vendo quantidade de jogadores
while True:
    jogadores = int(input('Defina a quantidade de jogadores: [1] ou [2] '))
    if jogadores == 1:
        #Criando a Tabela de Informações do Jogo com a quantidade de jogadores
        print(Fore.BLUE)
        nome = input('Nome: ')
        tabela = PrettyTable()
        tabela = ColorTable(theme=Themes.OCEAN)
        tabela.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
        tabela.add_row([nome,len(tesouros_jogador1), tesouros_jogador1, 'qntidade_oxigenio'])
        print(tabela)
    elif jogadores == 2:
        nome1 = input('Nome do jogador 1: ')
        nome2 = input('Nome do jogador 2: ')
        tabela = PrettyTable()
        tabela = ColorTable(theme=Themes.OCEAN)
        tabela.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
        tabela.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, 'qntidade_oxigenio'])
        tabela.add_row([nome2,len(tesouros_jogador2), tesouros_jogador2, 'qntidade_oxigenio'])
        print(tabela)
    break
#Desenhando o mapa
print_slow('Inicializando mapa....')
print()
for e in tqdm([1,2,3,4,5,6,7,8,9]):
    sleep(0.5)
print(Fore.YELLOW)
print_slow('''
                                         ...                              
                                   .~!~^.                             
                                   :!!.                               
                                   :!!.                               
                                   :!!                                
                           ........:~~..                              
                           !777~~~~^^^~~.                             
                           !!~^^::::::::.....                         
               .^^^:     .:::.....:::::.:::......                     
               .~^^~: .::^:::::.:::::.:::::.....:^^:                  
               .~^~!^.:::^^^^^^::::::^^^^^^:::::^^^~^.                
                :^!7~^^^^^::::^^^:::^^:::^^^^::^^^^^^~.               
                .^!7~^^^^^::::^^^^^^~^::::^~^^^^^^^^^~.               
               .~^~7^:::^^^^^^^^:::::^^^^^^^:::^^^^^~:                
               .~^^~: ::::^^^^^::::::::::::..::::^~^.                 
               .~^^^.   .:::::::::::::::::::::::::.                   
                ...        ...:::::::::::::::..                       
                                    .. .                              ''')
print()
print(lista_posicao_tesouros)
#Iniciando o Jogo
while True:
    if jogadores == 1:
        while True:
            jogar_dados = ('Pressione [Enter] para rodar os dados: ')
            dados_jogados = sorteio_dados()
            print(Fore.BLUE)
            print(dados_jogados)
            #substituir o elemento sorteado por um bonequinho
    

            
