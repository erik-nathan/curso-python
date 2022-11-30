'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

print("="*41)
print("DESAFIO 65 - MAIOR E MENOR VALORES")
print("="*41)

s = cont = media = maior = menor = 0
fim = False
while not fim:
    num = int(input('Informe um número: '))
    s += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).upper()
    print("=-" * 20)
    if res == 'N': fim = True
media = s / cont
print('- Você digitou {} números e a média entre eles é: {}!'.format(cont, media))
print('- O maior valor foi {} e o menor foi {}!'.format(maior, menor))
