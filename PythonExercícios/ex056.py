'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

print("="*39)
print("DESAFIO 56 - ANALISADOR COMPLETO")
print("="*39)

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = 0
totMulher20 = 0
for c in range(1, 5):
    print('--- PESSOA DE NÚMERO {} ---'.format(c))
    name = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = name
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = name
    if sexo in 'fF' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print('Media da idade do grupo: {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}!'.format(maiorIdadeHomem, nomeVelho))
print('Mulheres com mais de 20 anos: {}'.format(totMulher20))
