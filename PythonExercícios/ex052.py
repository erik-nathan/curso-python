# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# (número natural é primo se ele é maior que 1 e é divisível apenas por si próprio e por 1.)

print("="*27)
print("DESAFIO 52 - NÚMEROS PRIMOS")
print("="*27)

num = int(input('Informe um número: '))
div = 0
for divisor in range(1, num):
    if num % divisor == 0:
        div = div + 1
        if div > 1:
            break
if div > 1:
    print('NÃO É PRIMO')
else:
    print('É PRIMO')

