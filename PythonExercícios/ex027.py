#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('============= DESAFIO 27 - Primeiro e último nome de uma pessoa ==============')
name = str(input('Informe seu nome completo: ')).strip()
n = name.split()
print('Primeiro nome: {}'.format(n[0]))
print('Seu ultimo nome: {}'.format(n[len(n)-1]))