'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista..'''

print("="*43)
print("DESAFIO 78 - MAIOR E MENOR VALORES NA LISTA")
print("="*43)

valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('=' * 30)
print(f'Você digitou ou valores  {valores}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()

print(f'O menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
