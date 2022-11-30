# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('============= DESAFIO 31 - Custo da Viagem ==============')
dist = float(input('Informe a distância da viagem: '))
if dist <= 200:
    cobrança1 = dist * 0.50
    print('Você receberar uma cobrança de {}'.format(cobrança1))
else:
    cobrança2 = dist * 0.45
    print('Você receberar uma cobrança de {}'.format(cobrança2))
