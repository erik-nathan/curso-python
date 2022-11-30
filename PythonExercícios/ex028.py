# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

print('============= DESAFIO 28 - Jogo da Adivinhação v.1.0 ==============')
import random
escolhido = random.randint(1, 5)
num = int(input('Escolha um número: '))
if num == escolhido:
    print('VOCÊ ACERTOU O NÚMERO ESCOLHIDO')
else:
    print('VOCÊ ERROU O NÚMERO')
print('O número que o computadou escolheu foi: {}'.format(escolhido))
