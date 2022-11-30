# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('============= DESAFIO 28 - Radar eletrônico ==============')
velocidade = float(input('Informe a sua velocidade: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (80 - velocidade) * -7
    print('A multa está no valor de {}'.format(multa))
else:
    print('Você está no limite da via')
