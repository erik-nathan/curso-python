'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

print('============= DESAFIO 41 - Classificando Atletas ==============')
from datetime import date
anoNasc = int(input('Informe o ano de nascimento: '))
age = date.today().year - anoNasc
print('Sua idade é:',age)
print('=='*24)

if age <= 9:
    print('Categoria MIRIM')
elif age <= 14:
    print('Categoria INFANTIL')
elif age <= 19:
    print('Categoria JÚNIOR')
elif age <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
