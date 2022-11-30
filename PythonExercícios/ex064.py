'''Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)..'''

print("="*41)
print("DESAFIO 64 - TRATANDO VÁRIOS VALORES V1.0")
print("="*41)

num = fim = s = cont = 0
print('Parar a contagem -> 999')
print("-" * 41)
while not fim:
    n = int(input('Informe um número: '))
    print("-" * 41)
    s += n
    cont += 1
    if n == 999:
        fim = 1
print('Foram digitados {} valores e soma deles foi: {}'.format(cont - 1, s - 999))
print(' - - - F I M - - - ')
