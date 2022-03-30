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
posicao_jogador1 = 0
posicao_jogador2 = 0
#Vendo quantidade de jogadores
while True:
    jogadores = int(input('Defina a quantidade de jogadores: [1] ou [2] '))
    #Criando a tabela de Informações do Jogo com a quantidade de jogadores
    if jogadores == 1:
        print(Fore.BLUE)
        nome = input('Nome: ')
        tabela_exemplo = PrettyTable()
        tabela_exemplo = ColorTable(theme=Themes.OCEAN)
        tabela_exemplo.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
        tabela_exemplo.add_row([nome,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
        print(tabela_exemplo)
    elif jogadores == 2:
        nome1 = input('Nome do jogador 1: ')
        nome2 = input('Nome do jogador 2: ')
        tabela_exemplo = PrettyTable()
        tabela_exemplo = ColorTable(theme=Themes.OCEAN)
        tabela_exemplo.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
        tabela_exemplo.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
        tabela_exemplo.add_row([nome2,len(tesouros_jogador2), tesouros_jogador2, oxigenio])
        print(tabela_exemplo)
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
        nickname = nome[0]
        #Rodando os dados e mudando a posição do jogador
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
            
            print(posicao_lista(lista_posicao_tesouros,posicao_jogador1,nickname))
            if (posicao_lista(lista_posicao_tesouros,posicao_jogador1,nickname)) == "Redirecionando o personagem.":
                posicao_jogador1 = 32
                while posicao_jogador1 > 1:
                    print(Fore.BLUE)
                    dado1_volta = sorteio_dado1()
                    print_slow(f'O primeiro dado caiu no número: {dado1_volta}')
                    print()
                    dado2_volta = sorteio_dado2()
                    print_slow(f'O segundo dado caiu no número: {dado2_volta}')
                    print()
                    dados_jogados_volta = dado1_volta + dado2_volta
                    print(f'A soma dos dados é {dados_jogados}')
                    print(Fore.YELLOW)
                    print(retorne_posicao(lista_posicao_tesouros,posicao_jogador1,nickname))
                    posicao_jogador1 -= dados_jogados
                    print(Fore.BLUE)
                    if len(tesouros_jogador1) < 4:
                        ganhou_tesouro = sorteio_tesouros(posicao_jogador1)
                        print(Fore.BLUE)
                        print_slow(f'Tesouro encontrado no valor de: {ganhou_tesouro}')
                        print()
                        print_slow('Deseja ficar com o tesouro?:  ')
                        print()
                        pergunta_tesouro = input('[S] / [N]: ').upper()
                        if pergunta_tesouro == 'S':
                            tesouros_jogador1.append(ganhou_tesouro)
                            tabela_jg1 = PrettyTable()
                            tabela_jg1 = ColorTable(theme=Themes.OCEAN)
                            tabela_jg1.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
                            tabela_jg1.add_row([nome,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
                            print(tabela_jg1)
                        else:
                            print_slow('Tesouro não coletado')
                    else:
                        ganhou_tesouro = sorteio_tesouros(posicao_jogador1)
                        print(Fore.BLUE)
                        print_slow(f'Tesouro encontrado no valor de: {ganhou_tesouro}')
                        print()
                        print_slow('Número máximo de tesouros recolhidos, deseja remover um para guardar este? [S] / [N]: ')
                        print()
                        pergunta_tesouro_cheio = input('').upper()
                        if pergunta_tesouro_cheio == 'S':
                            print_slow('Digite o Tesouro que deseja remover: ')
                            print()
                            num_tesouro_remover = int(input(''))
                            posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                            tesouros_jogador1[posicao_tesouro] = ganhou_tesouro
                            print(tabela_jg1)
            elif posicao_jogador1 < 1:
                pergunta_submarino = input('Deseja retornar para o submarino? [S] / [N] ').upper()
                if pergunta_submarino == 'S' and oxigenio > 0:
                    print('Retornando para o submarino, jogo finalizado!')
                    print(tabela_jg1)
                    break
                


                    

            elif len(tesouros_jogador1) < 4:
                ganhou_tesouro = sorteio_tesouros(posicao_jogador1)
                print(Fore.BLUE)
                print_slow(f'Tesouro encontrado no valor de: {ganhou_tesouro}')
                print()
                print_slow('Deseja ficar com o tesouro?:  ')
                print()
                pergunta_tesouro = input('[S] / [N]: ').upper()
                if pergunta_tesouro == 'S':
                    tesouros_jogador1.append(ganhou_tesouro)
                    tabela_jg1 = PrettyTable()
                    tabela_jg1 = ColorTable(theme=Themes.OCEAN)
                    tabela_jg1.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio']
                    tabela_jg1.add_row([nome,len(tesouros_jogador1), tesouros_jogador1, oxigenio])
                    print(tabela_jg1)
                else:
                    print_slow('Tesouro não coletado')
            else:
                ganhou_tesouro = sorteio_tesouros(posicao_jogador1)
                print(Fore.BLUE)
                print_slow(f'Tesouro encontrado no valor de: {ganhou_tesouro}')
                print()
                print_slow('Número máximo de tesouros recolhidos, deseja remover um para guardar este? [S] / [N]: ')
                print()
                pergunta_tesouro_cheio = input('').upper()
                if pergunta_tesouro_cheio == 'S':
                    print_slow('Digite o Tesouro que deseja remover: ')
                    print()
                    num_tesouro_remover = int(input(''))
                    posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                    tesouros_jogador1[posicao_tesouro] = ganhou_tesouro
                    print(tabela_jg1)
                else:
                    break
    break
    

            

