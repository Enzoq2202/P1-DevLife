#Importando bibliotecas
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
        print(Fore.WHITE)
        print_slow('Escolha um mergulhador profundo do mar, role os dados e mergulhe no oceano')
        print()
        print_slow('Adquira sua fortuna: pouse em um pedaço de tesouro para adicioná-lo à sua coleção. Quanto mais fundo você for, mais valioso pode ser seu tesouro.')
        print()
        print_slow('Não fique muito pegajoso: todos os mergulhadores têm um suprimento compartilhado de oxigênio. Então, se você passar muito tempo procurando tesouros, você pode ficar preso lá de vez.')
        print()
        break
    elif pergunta_tutorial == 'N':
        print(Fore.BLUE)
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
#Perguntando a quantidade de jogadores.
qntidade_jogadores = int(input('Defina a quantidade de jogadores. [1] ou [2]: '))

if qntidade_jogadores == 1:
    nome1 = input('Digite seu nome: ')
    nickname_jogador1 = nome1[0]
else:
    nome1 = input('Digite seu nome: ')
    nickname_jogador1 = nome1[0]
    nome2 = input('Digite seu nome: ')
    nickname_jogador2 = nome2[0]


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
posicao_jogador1 = 0
posicao_jogador2 = 0
retroceder_jogador1 = False
retroceder_jogador2 = False

#Criando as tabelas que vão armazenar as informações dos jogadores.
if qntidade_jogadores == 1:
    tabela_1_jogador = PrettyTable()
    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
    print(tabela_1_jogador)
else:
    tabela_2_jogadores = PrettyTable()
    tabela_2_jogadores = ColorTable(theme=Themes.OCEAN)
    tabela_2_jogadores.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
    tabela_2_jogadores.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
    tabela_2_jogadores.add_row([nome2,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
    print(tabela_2_jogadores)
#Desenhando o mapa
print_slow('Inicializando mapa....')
print()
print(Fore.WHITE)
for e in tqdm([1,2,3,4,5,6,7,8,9]):
    sleep(0.25)
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

#Inciando o jogo para 1 jogador
if qntidade_jogadores == 1:
    while True:
        print(Fore.BLUE)
        jogar_dados = ('Pressione [Enter] para rodar os dados: ')
        dado1 = sorteio_dado1()
        dado2 = sorteio_dado2()
        print_slow(f'O primeiro dado caiu no número: {dado1}')
        print()
        print_slow(f'O segundo dado caiu no número: {dado2}')
        print()
        dados_jogados = dado1 + dado2
        posicao_jogador1+=dados_jogados
        print(Fore.BLUE)
        print(dados_jogados)
        print_slow('Voçê se encontra nesta posição: ')
        print()
        print(Fore.YELLOW)
        print('''
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
            
        print(posicao_lista(lista_posicao_tesouros,posicao_jogador1,nickname_jogador1))
        valor_tesouro = sorteio_tesouros(posicao_jogador1)
        pergunta_tesouro = input(f'Deseja pegar o tesouro de valor [{valor_tesouro}]? [S] / [N]: ').upper()
        if pergunta_tesouro == 'S' and len(tesouros_jogador1) < 4:
            tesouros_jogador1.append(valor_tesouro)
            tabela_1_jogador = PrettyTable()
            tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
            tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
            tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
            print(tabela_1_jogador)
        elif pergunta_tesouro == 'S' and len(tesouros_jogador1) >= 4:
            pergunta_remover_tesouro = (f'Quantidade máxima de tesouros atingidas, deseja remover um tesouro para adicionar este de valor {valor_tesouro}? [S] / [N]: ')
            if pergunta_remover_tesouro == 'S':
                num_tesouro_remover = int(input(''))
                posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                tesouros_jogador1[posicao_tesouro] = valor_tesouro
                print(tabela_1_jogador)
        else:
            print('Tesouro não coletado')

        
        
        
        
        
        #break #while principal