'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def title(text):
    tam = len(text)
    print('=' *tam)
    print(f'{text.upper()}')
    print('=' *tam)
title("Exercício Python #103 - Ficha do Jogador")

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')

n = str(input("Nome do Jogador: "))
g = str(input("Número do Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

