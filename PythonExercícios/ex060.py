'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

print("="*32)
print("DESAFIO 60 - CÁLCULO DO FATORIAL")
print("="*32)

from math import factorial
num = int(input('Informe o número para calular o fatorial: '))
r = factorial(num)
c = num
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(r)
