'''Crie um programa que faça o computador jogar Jokenpô com você!'''

print('============= DESAFIO 45 - GAME: Pedra Papel e Tesoura ==============')
from random import choice
print('[PEDRA] | [PAPEL] | [TESOURA]')
print('--'*24)
aux = str(input('Escolha uma opção: '))
jokenpo = choice(['pedra', 'papel', 'tesoura'])
print('Máquina: ',jokenpo)
print('=='*24)

if aux == 'pedra' and jokenpo == 'tesoura' or aux == 'papel' and jokenpo == 'pedra' or aux == 'tesoura' and jokenpo == 'papel':
    print('VOCÊ GANHOU!!!')
elif aux == 'pedra' and jokenpo == 'pedra' or aux == 'papel' and jokenpo == 'papel' or aux == 'tesoura' and jokenpo == 'tesoura':
    print('EMPATOU!!!')
else:
    print('VOCÊ PERDEU!!!')