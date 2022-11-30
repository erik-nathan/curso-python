'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1..'''

print("="*42)
print("DESAFIO 71 - SIMULADOR DE CAIXA ELETRÔNICO")
print("="*42)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totCéd = 0
while True:
    if total >= céd:
        total -= céd
        totCéd += 1
    else:
        if totCéd > 0:
            print(f'Total de {totCéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totCéd = 0
        if total == 0:
            break
print('-'*30)
print('VOLTE SEMPRE!')