#Projeto: Jogo da Forca

#aluno: Ewerton da Silva Costa
#email: ewertonavlis@gmail.com
#turma: 889
# Módulo 2 - LÓGICA DE PROGRAMAÇÃO II (PY) - <Div>ersidade Tech - Let's Code by Ada

import os 
import random

ERRO_0 = ("""
    |-------
    |      |
    |    
    |    
    |    
    |     
    |     
 ___|___ 
  """)
ERRO_1 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |      
    |     
    |     
 ___|___ 
  """)

ERRO_2 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |      |
    |      |
    |     
 ___|___ 
  """)

ERRO_3 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |    --|
    |      |
    |     
 ___|___ 
  """)

ERRO_4 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     
 ___|___ 
  """)

ERRO_5 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     / 
 ___|___ 
  """)

ERRO_6 = ("""
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     / \\
 ___|___ 
  """)
def boas_vindas():
    '''Cumprimenta o usuário'''
    print('\n')
    print("#############################################")
    print("######## Bem-Vind@ ao Jogo da Forca! ########")
    print("#############################################")

def menu():
    '''Imprime as opçoes para o usuário'''
    boas_vindas()
    print('1. Começar a jogar')
    print('2. Jogar Novamente')
    print('0. Sair')

def importando_arquivo(diretorio,nome) ->list:
    '''Recebe o diretorio e o nome do arquivo de banco de palavras
    '''
    caminho = os.path.join(diretorio,nome)
    try:
        with open(caminho, 'r', encoding='utf-8') as frutas:
            return frutas.readlines()
    except FileNotFoundError:
        print('Arquivo do banco de palavras não foi encontrado.')
        return []

def escolhe_palavra(arquivo:list) -> str:
    '''Recebe o arquivo com o banco de palavras e retorna
    uma palavra selecionada aleatoriamente
    '''
    posicao_palavra_aleatoria = random.randint(0,len(arquivo))
    palavra_escolhida = arquivo[posicao_palavra_aleatoria].replace('\n','')
    return palavra_escolhida

def imprime_(palavra:str)-> str:
    '''Recebe a palavra selecionada e imprime _ referente a quatidade de letras e
    retorna uma string nesse formato
    '''
    print('\n')
    print('A fruta escolhida foi: ',end='')
    print('_ '*len(palavra), end='')
    print('\n')
    return '_ '*len(palavra)

def posicao_na_palavra(arquivo:str,letra:str) -> list:
    '''Recebe a palavra escolhida e a letra informada pela pessoa usuária e
    verifica em qual (ais) posição (ões) está (ão).
    '''
    contador = 0
    posicao = []
    for letras in arquivo:
        if letras == letra:
            posicao.append(contador)
        #Considera os espaços em branco. '_' + ' '
        contador += 2
    return posicao

def remove_(palavra:str,letra:str,palavra_atualizada:str) -> str:
    '''Recebe a palavra selecionada e a letra escolhida pela pessoa usuária
    e remove _ referente a quatidade de letras que estão contidas na palavra
    selecionada
    '''
    posicao = posicao_na_palavra(palavra,letra)
    palavra_modificada = ''
    #Considera os espaços em branco. '_' + ' '
    for idx in range(0,2*len(palavra),2):
        if idx in posicao:
            palavra_modificada += letra + ' '
        else:
            if palavra_atualizada[idx] == '_':
                palavra_modificada += '_' + ' '  
            elif palavra_atualizada[idx] != ' ':
                palavra_modificada += palavra_atualizada[idx] + ' '
    print(f'\nA letra: {letra} está em: ', end=' ')
    print(f'{palavra_modificada}',end=' ')
    print('\n')
    return palavra_modificada

def trata_letra_escolhida() -> str:
    '''Recebe um input da pessoa usuária e verifica se é uma letra válida
    '''
    caracteres_especiais = "/^`()?!=.*+-,_ ;[]'{''}'0123456789@#$%&"
    while True:
        letra = input('Escolha uma letra e tente acertar a fruta: ')
        if letra in caracteres_especiais[:]:
            print('Digite apenas letras do alfabeto.\n')
        elif len(letra) > 1:
            print('Digite apenas uma letra.\n')
        else:
            break
    return letra.lower()

def  limpa_terminal():
    '''Limpa o terminal
    '''
    if os.name == 'nt':
        #for windows
        _=os.system('cls' )
    else:
        #for mac and linux(here, os.name is 'posix')
        _=os.system('clear')
    
def chuta_palavra(fruta:str,palavra_auxiliar:str,qtd_erros:int,forca:list,end:bool) ->(bool,int):
    '''Recebe informação do programa para perguntar se a pessoa usuária deseja
    chutar qual a palavra escolhida
    '''
    letras_faltando = [string for string in palavra_auxiliar if string == '_']
    if len(letras_faltando) <= 4 and len(letras_faltando) > 1:
        chute = False
        while not chute:
            tentativa = input('Deseja chutar qual a fruta? ')
            if tentativa.lower() in ['s','sim','y','yes']:
                chutando = input('Qual a fruta? ')
                if chutando in fruta:
                    print(f'\nParabéns! Você adivinhou que a fruta era: {fruta}\n')
                    chute = True
                    end = True
                else:
                    limpa_terminal()
                    print(f'\nVocê errou! Tente novamente: {palavra_auxiliar}\n')
                    print(forca[qtd_erros])
                    qtd_erros += 1
                    chute = True
            else:
                chute = True
    return end,qtd_erros

def letra_certa(fruta:str,letra:str,palavra_auxiliar:str,letra_ja_selecionada:list,end:bool)->(str,list,bool): 
    '''Recebe a letra que a pessoa usuária acerto e atualiza na palavra a ser advinhada
    '''
    if letra not in letra_ja_selecionada:
        palavra_auxiliar = remove_(fruta,letra,palavra_auxiliar)
        letra_ja_selecionada.append(letra)
        if palavra_auxiliar.replace(' ','') in fruta:
            print(f'\nParabéns! Você adivinhou que a fruta era: {fruta}\n')
            end = True
    else:
        print(f'\nA letra: {letra} já foi selecionada. Escolha outra.\n')
    return palavra_auxiliar,letra_ja_selecionada,end

def letra_errada(fruta:str,letra:str,palavra_auxiliar:str,forca:list,qtd_erros:int,erros:list,opcao:str)->(int,str,list):
    '''Informa a pessoa usuária se a letra não está na palavra a ser advinhada
    ou se o número máximo de  tentativas foi atingido
    '''
    print(f'\nVocê errou! Tente novamente: {palavra_auxiliar}\n')
    print(forca[qtd_erros])
    erros.append(letra)
    qtd_erros += 1
    opcao = parada(qtd_erros,fruta,opcao)
    print(f'Erros: {erros}. Você tem {len(forca)-qtd_erros} tentativas')
    return qtd_erros,opcao,erros

def parada(qtd_erros:int,fruta:str,opcao:str) -> str:
    '''Para o programa quando o número máximo de erros é atingido
    '''
    if qtd_erros == 7:
        print(f'\nVocê perdeu! A palavra era: {fruta}\n')
        opcao = 'fim'
    return opcao

def main():
    '''Função principal. Chama as outras funcionalidades para simular 
    o jogo da forca
    '''
    forca = [ERRO_0,ERRO_1,ERRO_2,ERRO_3,ERRO_4,ERRO_5,ERRO_6]
    arquivo = importando_arquivo('./','frutas.txt')

    boas_vindas()
    end = False
    opcao = 'inicio'
    while not end:
        if opcao == 'inicio':
            fruta = escolhe_palavra(arquivo)
            palavra_auxiliar = imprime_(fruta)
            qtd_erros = 0
            erros = []
            letra_ja_selecionada = []
            opcao = 'jogando'
        elif opcao == 'jogando':
            letra = trata_letra_escolhida()
            if letra in fruta:
                limpa_terminal()
                palavra_auxiliar,letra_ja_selecionada,end = letra_certa(fruta,letra,palavra_auxiliar,letra_ja_selecionada,end)
                end,qtd_erros = chuta_palavra(fruta,palavra_auxiliar,qtd_erros,forca,end)
            else:
                limpa_terminal()
                qtd_erros,opcao,erros = letra_errada(fruta,letra,palavra_auxiliar,forca,qtd_erros,erros,opcao)
            opcao = parada(qtd_erros,fruta,opcao)
        elif opcao == 'fim':
            print('Até mais. Volte sempre!')
            end = True 
main()
