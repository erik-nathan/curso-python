'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso..'''

print("="*31)
print("DESAFIO 72 - NÚMERO POR EXTENSO")
print("="*31)

from random import randint
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Informe um número entre 0 - 20: '))
    if n > 20 or n < 0:
        print('Tente novamente!')
        print("-" * 30)
        continue
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}')
        print("-" * 30)
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print("-" * 30)
        if continuar == 'S':
            continue
        elif continuar == 'N':
            print('Programa encerrado..!')
            break