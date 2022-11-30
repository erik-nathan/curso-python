#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('============= DESAFIO 26 - Primeira e última ocorrência de uma string ==============')
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aprecere {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aprecereu na posição {}.'.format(frase.find('A')+1))
print('A última letra A aprecereu na posição {}.'.format(frase.rfind('A')+1))

