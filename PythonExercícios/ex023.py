#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('============= DESAFIO 23 - Separando dígitos de um número ==============')
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centeza: {}'.format(c))
print('Milhar: {}'.format(m))
