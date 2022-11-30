'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores'''

print("="*32)
print("DESAFIO 54 - GRUPO DA MAIORIDADE")
print("="*32)

from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totMaior += 1
    else:
        totMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totMaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totMenor))
