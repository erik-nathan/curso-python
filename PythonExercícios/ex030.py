# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('============= DESAFIO 30 - Par ou Ímpar ==============')
num = int(input('Informe um número: '))
resto = num % 2
if resto == 0:
    print('Você informou um número PAR!')
else:
    print('Você informou um número ÍMPAR!')
