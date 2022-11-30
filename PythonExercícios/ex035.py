# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('============= DESAFIO 35 - Analisando Triângulo v1.0 ==============')
trian1 = float(input('Informe o comprimento 1: '))
trian2 = float(input('Informe o comprimento 2: '))
trian3 = float(input('Informe o comprimento 3: '))

if trian1 < trian2 + trian1 and trian2 < trian1 + trian3 and trian3 < trian1 + trian2:
    print('Os comprimentos citados podem se torna um triângulo!')
else:
    print('Os comprimentos citados não podem se tornar um triângulo!')
