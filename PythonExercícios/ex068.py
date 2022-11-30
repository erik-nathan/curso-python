'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.'''

print("="*33)
print("DESAFIO 68 - JOGO DO PAR OU ÍMPAR")
print("="*33)

from random import randint
cont = 0
while True:
    player = int(input('Informe um valor: '))
    numPc = randint(0, 11)
    soma = player + numPc
    ParImp = ' '
    while ParImp not in 'IP':
        ParImp = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {player} e o computador {numPc}. Total de {soma}')
    if ParImp == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif ParImp == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            print("-" * 33)
            break
    print('Vamos jogar novamente?..')
    print("-" * 33)
print(f'GAME OVER! Você venceu {cont} vezes!')

