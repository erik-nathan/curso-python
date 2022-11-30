'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def title(text):
    tam = len(text)
    print('=' *tam)
    print(f'{text}')
    print('=' *tam)
title("DESAFIO 99 - Função que descobre o maior")

from time import sleep

def maior(* num): 
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior valor infonrmado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
