'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

print("="*36)
print("DESAFIO 96 - Função que calcula área")
print("="*36)

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A largura do terrmo é igual á {a}')

l = float(input('Informe a largura: '))
c = float(input('Informe o comprimento: '))
area(l, c)
