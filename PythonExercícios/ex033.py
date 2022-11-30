# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('============= DESAFIO 33 - Maior e menor valores ==============')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

# número mais alto
maior = n1
if n1 > n2:
    maior = n2
if n3 > maior:
    maior = n3
print('Número maior é: {}'.format(maior))

# número menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('Número menor é: {}'.format(menor))
