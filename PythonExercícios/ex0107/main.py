'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

def title(text):
    tam = len(text)
    print('=' *tam)
    print(f'{text.upper()}')
    print('=' *tam)
title("Exercício Python #107 - Exercitando módulos em Python")

p = float(input('Informe o preço: R$'))
# print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O docbro de R${p} é R${moeda.dobro}')
