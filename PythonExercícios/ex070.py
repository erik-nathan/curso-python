'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print("="*37)
print("DESAFIO 70 - ESTATÍSTICAS EM PRODUTOS")
print("="*37)

fim = False
totGasto = maiorMil = menor = cont = 0
prodBarato = ''
while not fim:
    nome = str(input('Informe o nome do produto: '))
    preço = float(input('Informe o preço do produto: R$'))
    cont += 1
    print("-" * 30)
    totGasto += preço
    if preço > 1000:
        maiorMil += 1
        prodBarato = nome
    if cont == 1 or preço < menor:
        menor = preço
        prodBarato = nome
    aux = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print("-" * 30)
    if aux == 'N':
        fim = True
print(f'Valor total gasto na compra: R${totGasto:.2f}')
print(f'Quantidade de produtos com valor acima de 1000: {maiorMil}')
print(f'O produto mais barato foi {prodBarato} que custa: R${menor:.2f}')
