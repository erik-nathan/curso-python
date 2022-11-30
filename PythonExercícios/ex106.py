'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

from termios import CINTR


def title(text):
    tam = len(text)
    print('=' *tam)
    print(f'{text.upper()}')
    print('=' *tam)
title("Exercício Python #106 - Sistema interativo de ajuda em Python")

def ajuda(com):
    help(com)

def título(msg, cor):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# PROGRAMA PRINCIPAL
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!')