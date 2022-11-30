'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

print("="*38)
print("DESAFIO 69 - ANÁLISE DE DADOS DO GRUPO")
print("="*38)

from time import sleep
fim = False
maior18 = contHom = totMulher20 = 0
while not fim:
    num = int(input('Informe a idade: '))
    if num > 18:
        maior18 += 1
    sexo = str(input('Informe o sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        contHom += 1
    elif sexo == 'F' and num > 20:
        totMulher20 += 1
    print("-" * 30)
    aux = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print("-" * 30)
    if aux == 'N':
        fim = True

print('Encerrando o programa...')
sleep(1.5)
print("-" * 30)
print(f'Maiores de 18 anos: {maior18}')
print(f'Total de homens cadastrados: {contHom}')
print(f'Mulheres acima de 20 anos: {totMulher20}')
