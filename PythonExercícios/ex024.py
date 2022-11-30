#  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('============= DESAFIO 24 - Verificando as primeiras letras de um texto ==============')

cid = str(input('Em que cidade você nasceu: ')).strip()

print(cid[:5].upper() == 'SANTO')
