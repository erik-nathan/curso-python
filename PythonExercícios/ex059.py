'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso..'''

print("="*38)
print("DESAFIO 59 - CRIANDO UM MENU DE OPÇÕES")
print("="*38)

from time import sleep
valueOne = int(input('Informe o primeiro valor: '))
valueTwo = int(input('Informe o segundo valor: '))
print('-'*35)
fim = False
while not fim:
    menu = int(input('Escola uma das opções:'
                     '\n[1] SOMAR '
                     '\n[2] MULTIPLICAR'
                     '\n[3] MAIOR'
                     '\n[4] NOVOS NÚMEROS'
                     '\n[5] SAIR DO PROGRAMA'
                     '\n- Opção: '))
    soma = valueOne + valueTwo
    multi = valueOne * valueTwo
    print('-'*35)

    # SOMA
    if menu == 1:
        print('A soma entre o valor {} e {} é: {}'.format(valueOne, valueTwo, soma))
        print('-' * 35)

    # MULTIPLICAÇÃO
    elif menu == 2:
        print('A multiplicação entre os valores {} e {} é: {}'.format(valueOne, valueTwo, multi))
        print('-' * 35)

    # MAIOR NUMERO
    elif menu == 3:
        maior = valueOne
        if valueOne > valueTwo:
            maior = valueOne
            print('O maior número entre os valores {} e {} é: {}'.format(valueOne, valueTwo, maior))
            print('-' * 35)
        if valueTwo > valueOne:
            maior = valueTwo
            print('O maior número entre os valores {} e {} é: {}'.format(valueOne, valueTwo, maior))
            print('-' * 35)
        if valueOne == valueTwo:
            print('Os valores são iguais!')
            print('-' * 35)

    # NOVOS NÚMEROS
    elif menu == 4:
        print('Você quer escolher novos valores? Ok!')
        valueOne = int(input('Informe o primeiro valor: '))
        valueTwo = int(input('Informe o segundo valor: '))

    # FINALIZAR
    elif menu == 5:
        print('Ok! Estarei finalizar o programa em alguns segundos!')
        sleep(3)
        fim = True

print('-'*40)
print(' - - - F I M  D O  P R O G R A M A - - - ')
print('-'*40)
