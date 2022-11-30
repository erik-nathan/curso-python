'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

print("="*39)
print("DESAFIO 55 - MAIOR E MENOR DA SEQUÊNCIA")
print("="*39)

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso: '))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi: {}'.format(maior))
print('O menor peso foi: {}'.format(menor))
