#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('============= DESAFIO 25 - Procurando uma string dentro de outra ==============')

name = str(input('Informe o nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in name.upper()))