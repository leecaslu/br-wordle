from random import (
    choice
)
from colorama import Fore as Fr


def escolha():
    """
    Função que escolhe a palavra do dia
    :return: uma palavra de 5 letras em português
    """
    with open('lista de palavras') as file:
        text = file.read().split('\n')
    alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')
    while True:
        palavra = choice(text)
        if all(map(lambda x: x in alfabeto, palavra)):
            return palavra


def tentativa():
    alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')
    while True:
        guess = input(f'Insira uma palavra de 5 letras')
        if not all(map(lambda letra: letra in alfabeto, tuple(guess))):
            print(f'A palavra deve conter apenas letras do alfabeto!')
        else:
            if len(guess) != 5:
                print('A palavra precisa ter 5 letras!')
            else:
                while True:
                    conf = input(f'A palavra que você quer é {guess}?\nAperte 1. para Sim e 2. para Não')
                    if conf == '1':
                        return guess
                    if conf == '2':
                        break


def gabarito(p_do_dia, resposta):
    saida = [' ', ' ', ' ', ' ', ' ']
    p_do_dia1 = list(p_do_dia)
    resposta1 = list(resposta)
    for i in range(5):
        if resposta[i] == p_do_dia[i]:
            saida[i] = Fr.GREEN + resposta[i]
            p_do_dia1[i] = ''
            resposta1[i] = ''
    for i in range(5):
        if resposta1[i] in p_do_dia1 and resposta1[i] != '':
            saida[i] = Fr.YELLOW + resposta[i]
            p_do_dia1[p_do_dia.index(resposta[i])] = ''
            resposta1[i] = ''
        elif resposta1[i] not in p_do_dia1:
            saida[i] = Fr.RED + resposta[i]
    return ''.join(saida) + Fr.RESET

def teste():
    print(gabarito('torso', 'barco'))
    print(gabarito('torso', 'porre'))
    print(gabarito('torso', 'tiros'))
    print(gabarito('torso', 'turno'))
    print(gabarito('barco', 'porto'))
    print(gabarito('barco', 'barco'))
    print(gabarito('barco', 'aaooo'))
    print(gabarito('barco', 'bbrco'))


if __name__ == '__main__':
    teste()
