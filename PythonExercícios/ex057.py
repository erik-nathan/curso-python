'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

print("="*31)
print("DESAFIO 57 - VALIDAÇÃO DE DADOS")
print("="*31)

sexo = input('Informe o Sexo [M/F] ').upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
