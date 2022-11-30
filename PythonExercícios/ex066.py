'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre elas (desconsiderando o flag).'''

print("="*36)
print("DESAFIO 66 - VÁRIOS NÚMEROS COM FLAG")
print("="*36)

s = cont = 0
while True:
    num = int(input('Informe um número: '))
    cont += 1
    if num == 999:
        break
    s += num
print(f'Você digitou {cont} números e a soma entre eles é de {s}')
