'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer..'''

print("="*35)
print("DESAFIO 58 - JOGO DE ADVINHAÇÃO V.2")
print("="*35)

from random import randint
pensador = randint(0, 10)
print('SOU SEU COMPUTADOR, ACABEI DE PENSAR EM UM NÚMERO ENTRE E 10')
print('SERÁ QUE VOCÊ CONSEGUE ACERTAR QUAL FOI?')
acertou = False
c = 0
while not acertou:
    num = int(input('Informe um número de 0 a 10: '))
    c += 1
    if num == pensador:
        acertou = True
        print('Você acertou!!')
    else:
        if num < pensador:
            print('Mais... Tente outra vez!')
            print('-'*35)
        elif num > pensador:
            print('Menos... Tente outra vez!')
            print('-'*35)
print('Você acertou com {} tentativas!'.format(c))
