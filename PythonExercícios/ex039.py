'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('============= DESAFIO 39 - Alistamento Militar ==============')

from datetime import date
birthYear = int(input('Informe o ano de nascimento: '))
years = date.today().year
age = years - birthYear
print('=='*24)

if age < 18:
    print('AINDA VAI SE ALISTAR')
    print('Você vai se ALISTAR dentro de {} ano(s), em {}.'.format(18 - age, years + (18 - age)))
elif age == 18:
    print('HORA EXATA DE SE ALISTAR')
else:
    print('JÁ PASSOU DO TEMPO DE ALISTAMENTO')
    print('Você deveria ter se ALISTADO há {} ano(s), em {}.'.format(age - 18, years - (age - 18)))
