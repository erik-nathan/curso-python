# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (se  m considerar espaços).
#  – Quantas letras tem o primeiro nome.

print('============= DESAFIO 22 - Analisador de Textos  ==============')
name = str(input('Informe seu nome: ')).strip()
print('Maiúsculas: ',name.upper())
print('Minúscula: ',name.lower())
print('Letras ao todo: ',len(name)-name.count(' '))
print('Letras do primeiro nome: ',name.find(' '))
