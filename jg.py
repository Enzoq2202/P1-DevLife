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
pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
pontuacao_final_jogador2 = pontuacao_final(tesouros_jogador2)
#Criando as tabelas que vão armazenar as informações dos jogadores.
if qntidade_jogadores == 1:
    tabela_1_jogador = PrettyTable()
    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
    print(tabela_1_jogador)
else:
    tabela_2_jogadores = PrettyTable()
    tabela_2_jogadores = ColorTable(theme=Themes.OCEAN)
    tabela_2_jogadores.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
    tabela_2_jogadores.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
    tabela_2_jogadores.add_row([nome2,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador2])
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
while True:
    print(tabela_1_jogador)
    if qntidade_jogadores == 1:
        while True:
            print(Fore.BLUE)
            avancar_retroceder = input('Para sair do submarino aperte [A] --> Avançar. ').upper()
            if avancar_retroceder != 'A':
                print(Fore.RED)
                print('Entrada Inválida, digite novamente.')
            else:
                break
        while True:
            print(Fore.BLUE)
            #Verificando se o jogador quer avançar ou retroceder
            while avancar_retroceder != 'R':
                print(Fore.BLUE)
                oxigenio -= len(tesouros_jogador1)
                if oxigenio <= 0:
                    print(Fore.GREEN)
                    print('Voçê perdeu, seu oxigênio ficou zerado! ')
                    print(Fore.BLUE)
                    break
                else:
                    tabela_1_jogador = PrettyTable()
                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                    print(f'Nesta rodada voçê perdeu {len(tesouros_jogador1)} oxigênios. ')
                    print(tabela_1_jogador)
                print(Fore.BLUE)
                jogar_dados = ('Pressione [Enter] para rodar os dados: ')
                dado1 = sorteio_dado1()
                dado2 = sorteio_dado2()
                print_slow(f'O primeiro dado caiu no número: {dado1}')
                print()
                print_slow(f'O segundo dado caiu no número: {dado2}')
                print()
                print(Fore.BLUE)
                soma_dos_dados = dado1 + dado2
                if len(tesouros_jogador1) == 0:
                    posicao_jogador1+=soma_dos_dados
                elif len(tesouros_jogador1) > 0:
                    soma_dos_dados -= len(tesouros_jogador1)
                    if soma_dos_dados <= 0:
                        posicao_jogador1 = posicao_jogador1
                    else:
                        posicao_jogador1 += soma_dos_dados
                else:
                    pass
                if posicao_jogador1 >= 32:
                    posicao_final = input('Voçê se encontra na última posição [32]. Deseja vasculhar esta região? [S] / [N]. Após a resposta voçê será automaticamente redirecionado ao caminho de volta para o submarino, não podendo mais avançar para frente. ').upper()
                    if posicao_final == 'S':
                        if len(tesouros_jogador1) < 4:
                                valor_tesouro = sorteio_tesouros(posicao_jogador1)
                                print(Fore.CYAN)
                                print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                                quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                                print(Fore.BLUE)
                                if quer_tesouro == 'S':
                                    tesouros_jogador1.append(valor_tesouro)
                                    tabela_1_jogador = PrettyTable()
                                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                                    posicao_jogador1 = 32
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
                                    avancar_retroceder = 'R'
                                else:
                                    print(Fore.BLUE)
                                    print('Tesouro não removido. ')
                        else:
                            valor_tesouro= sorteio_tesouros(posicao_jogador1)
                            print(Fore.BLUE)
                            print(f'Seus tesouros são: {tesouros_jogador1} ')
                            print('Número máximo de tesouros recolhidos, deseja remover um para guardar este? [S] / [N]: ')
                            pergunta_tesouro_cheio = input('').upper()
                            if pergunta_tesouro_cheio == 'S':
                                print(Fore.BLUE)
                                print('Digite o Tesouro que deseja remover: ')
                                num_tesouro_remover = int(input(''))
                                posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                                print(Fore.MAGENTA)
                                print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                                quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                                print(Fore.BLUE)
                                if quer_tesouro == 'S':
                                    print(Fore.BLUE)
                                    tesouros_jogador1[posicao_tesouro] = valor_tesouro
                                    tabela_1_jogador = PrettyTable()
                                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
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
                                else:
                                    print(Fore.BLUE)
                                    print('Tesouro não removido. ')
                    else:
                        posicao_jogador1 = 32
                        avancar_retroceder = 'R'
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


                else:
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
                    print(Fore.BLUE)
                    if len(tesouros_jogador1) > 0:
                        pergunta_dropar = input('Deseja remover algum tesouro para armazenar oxigênio? [S] / [N]: ').upper()
                        if pergunta_dropar == 'S':
                            print(tabela_1_jogador)
                            print(Fore.BLUE)
                            print('Digite o Tesouro que deseja remover: ')
                            num_tesouro_remover = int(input(''))
                            tesouros_jogador1.remove(num_tesouro_remover)
                            tabela_1_jogador = PrettyTable()
                            tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                            tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                            pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                            tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                        else:
                            print(Fore.BLUE)
                            print('Tesouro não removido. ')
                    posicao_final = input('Deseja vasculhar esta região em busca de tesouros? [S] / [N].  ').upper()
                    if posicao_final == 'S':
                        if len(tesouros_jogador1) < 4:
                                valor_tesouro = sorteio_tesouros(posicao_jogador1)
                                print(Fore.CYAN)
                                print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                                quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                                print(Fore.BLUE)
                                if quer_tesouro == 'S':
                                    print(Fore.BLUE)
                                    tesouros_jogador1.append(valor_tesouro)
                                    tabela_1_jogador = PrettyTable()
                                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                                else:
                                    print(Fore.BLUE)
                                    print('Tesouro não adicionado. ')
                        else:
                            valor_tesouro= sorteio_tesouros(posicao_jogador1)
                            print(Fore.BLUE)
                            print(f'Seus tesouros são: {tesouros_jogador1} ')
                            print('Número máximo de tesouros recolhidos, deseja remover um para guardar este? [S] / [N]: ')
                            pergunta_tesouro_cheio = input('').upper()
                            print(Fore.BLUE)
                            if pergunta_tesouro_cheio == 'S':
                                print(Fore.BLUE)
                                print('Digite o Tesouro que deseja remover: ')
                                num_tesouro_remover = int(input(''))
                                posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                                print(Fore.CYAN)
                                print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                                quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                                print(Fore.BLUE)
                                if quer_tesouro == 'S':
                                    print(Fore.BLUE)
                                    tesouros_jogador1[posicao_tesouro] = valor_tesouro
                                    tabela_1_jogador = PrettyTable()
                                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                                else:
                                    print(Fore.BLUE)
                                    print('Tesouro não removido. ')
                    else:
                        pass
                    print(Fore.BLUE)
                    avancar_retroceder = input('Como voçê deseja se locomover? : [A] --> Avançar [R] --> Retroceder. ').upper()



            if avancar_retroceder == 'R' and len(tesouros_jogador1) == 0 and posicao_jogador1 <= 1:
                print(Fore.GREEN)
                print('Não é possível retornar ao submarino, voçê não coletou nenhum tesouro.')
                print('Fim de jogo.')
                print(tabela_1_jogador)
                pergunta_reiniciar = input('Deseja reiniciar o jogo?: [S] / [N]. ').upper()
                break
            elif avancar_retroceder == 'R':
                print(Fore.MAGENTA)
                print_slow('Retrocedendo.................')
                print()
                print(Fore.BLUE)
                oxigenio -= len(tesouros_jogador1)
                if oxigenio <= 0:
                    print(Fore.GREEN)
                    print('Voçê perdeu, seu oxigênio ficou zerado! ')
                    print(Fore.BLUE)
                    print(tabela_1_jogador)
                    pergunta_reiniciar = input('Deseja reiniciar o jogo?: [S] / [N]. ').upper()
                    break
                else:
                    tabela_1_jogador = PrettyTable()
                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                    print(f'Nesta rodada voçê perdeu {len(tesouros_jogador1)} oxigênios. ')
                    print(tabela_1_jogador)
                print(Fore.BLUE)
                jogar_dados = ('Pressione [Enter] para rodar os dados: ')
                dado1 = sorteio_dado1()
                dado2 = sorteio_dado2()
                print_slow(f'O primeiro dado caiu no número: {dado1}')
                print()
                print_slow(f'O segundo dado caiu no número: {dado2}')
                print()
                print(Fore.BLUE)
                soma_dos_dados = dado1 + dado2
                print(f'A soma dos dados corresponde a {soma_dos_dados}')
                if len(tesouros_jogador1) == 0:
                    posicao_jogador1-=soma_dos_dados
                elif len(tesouros_jogador1) > 0:
                    soma_dos_dados -= len(tesouros_jogador1)
                    if soma_dos_dados <= 0:
                        posicao_jogador1 = posicao_jogador1
                        print(posicao_jogador1)
                    else:
                        posicao_jogador1 -= soma_dos_dados
                else:
                    pass
                if posicao_jogador1 < 1 and len(tesouros_jogador1) > 0:
                    print(Fore.GREEN)
                    print('Voçê se encontra na posição 0!')
                    print('Fim de jogo, voçê retornou ao submarino.')
                    pergunta_reiniciar = input('Deseja reiniciar o jogo?: [S] / [N]. ').upper()
                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                    tabela_1_jogador = PrettyTable()
                    tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                    tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                    pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                    tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                    print(tabela_1_jogador)
                    break
                else:
                    pass
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
                print(Fore.BLUE)
                print(f'Voçê se encontra na posição de número: {posicao_jogador1}')
                tabela_1_jogador = PrettyTable()
                tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                valor_tesouro = sorteio_tesouros(posicao_jogador1)
                if len(tesouros_jogador1) > 0:
                    pergunta_dropar = input('Deseja remover algum tesouro para armazenar oxigênio? [S] / [N]: ').upper()
                    if pergunta_dropar == 'S' and len(tesouros_jogador1) > 1:
                        print(tabela_1_jogador)
                        print(Fore.BLUE)
                        print('Digite o Tesouro que deseja remover: ')
                        num_tesouro_remover = int(input(''))
                        tesouros_jogador1.remove(num_tesouro_remover)
                        tabela_1_jogador = PrettyTable()
                        tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                        tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                        pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                        tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                    elif pergunta_dropar == 'S' and len(tesouros_jogador1) == 1:
                        print('Voçê não pode largar este tesouro, tendo em vista que possui apenas um e está no caminho de volta para o submarino. ')
                else:
                    pass

                print(Fore.BLUE)
                vasculhar_pergunta = input('Deseja vasculhar esta área e descobrir o valor de seu tesouro? [S] / [N]: ').upper()
                if vasculhar_pergunta == 'S':
                    if len(tesouros_jogador1) < 4:
                            valor_tesouro = sorteio_tesouros(posicao_jogador1)
                            print(Fore.CYAN)
                            print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                            quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                            print(Fore.BLUE)
                            if quer_tesouro == 'S':
                                print(Fore.BLUE)
                                tesouros_jogador1.append(valor_tesouro)
                                tabela_1_jogador = PrettyTable()
                                tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                            else:
                                print(Fore.BLUE)
                                print('Tesouro não removido. ')
                    else:
                        valor_tesouro= sorteio_tesouros(posicao_jogador1)
                        print(Fore.BLUE)
                        print(f'Seus tesouros são: {tesouros_jogador1} ')
                        print('Número máximo de tesouros recolhidos, deseja remover um para guardar este? [S] / [N]: ')
                        pergunta_tesouro_cheio = input('').upper()
                        if pergunta_tesouro_cheio == 'S':
                            print(Fore.BLUE)
                            print('Digite o Tesouro que deseja remover: ')
                            num_tesouro_remover = int(input(''))
                            posicao_tesouro = tesouros_jogador1.index(num_tesouro_remover)
                            print(Fore.CYAN)
                            print(f'Tesouro encontrado no valor de: {valor_tesouro}')
                            quer_tesouro = input('Deseja ficar com o tesouro? : [S] / [N]: ').upper()
                            print(Fore.BLUE)
                            if quer_tesouro == 'S':
                                print(Fore.BLUE)
                                tesouros_jogador1[posicao_tesouro] = valor_tesouro
                                tabela_1_jogador = PrettyTable()
                                tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
                                tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
                                pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
                                tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
                            else:
                                print(Fore.BLUE)
                                print('Tesouro não removido. ')
                else:
                    pass
    if pergunta_reiniciar == 'N':
        print(Fore.GREEN + 'Obrigado por jogar! ')
        break
    else:
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
        pontuacao_final_jogador1 = pontuacao_final(tesouros_jogador1)
        pontuacao_final_jogador2 = pontuacao_final(tesouros_jogador2)
        tabela_1_jogador = PrettyTable()
        tabela_1_jogador = ColorTable(theme=Themes.OCEAN)
        tabela_1_jogador.field_names = ['Jogadores', 'Quantidade de Tesouros', 'Tesouros', 'Oxigênio', 'Pontuação Final']
        tabela_1_jogador.add_row([nome1,len(tesouros_jogador1), tesouros_jogador1, oxigenio, pontuacao_final_jogador1])
        
        
        
        
        
        
        

