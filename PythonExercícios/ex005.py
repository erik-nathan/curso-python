# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

print('============ DESAFIO 05 ============')

n = int(input('Informe um número: '))

suc = n + 1
ant = n - 1

print('O sucessor de {} é {} e o antecessor é {}!'.format(n, suc, ant))