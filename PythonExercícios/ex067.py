'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

print("="*25)
print("DESAFIO 67 - TABUADA V3.0")
print("="*25)

from time import sleep
print('- - Para finalizar digite um número negativo! - -')
print('-' * 35)
while True:
    num = int(input('Informe um número para Tabuada: '))
    if num < 0 :
        break
    for c in range(1, 11):
        print(f'{num} x {c}: {num * c}')
    print('-' * 35)
print('-' * 35)
print('Encerrando o programa...')
sleep(3)
print(' - - - F I M - - - ')