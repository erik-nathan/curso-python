# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print('============= DESAFIO 32 - Ano Bissexto ==============')
from calendar import isleap
ano = int(input('Informe o ano: '))
if isleap(ano):
    print('ANO BISSEXTO')
else:
    print('NÃO É ANO BISSEXTO')
