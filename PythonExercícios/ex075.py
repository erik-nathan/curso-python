'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

print("="*41)
print("DESAFIO 75 - ANÁLISE DE DADOS EM UM TUPLA")
print("="*41)

c = 0
value = (int(input('Informe um número: ')),
          int(input('Informe outro número: ')),
          int(input('Informe mais um número: ')),
          int(input('Informe o último número: ')))
print(f'Você digitou os valores {value}')
print(f'O número 9 apareceu {value.count(9)} vezes')
if 3 in value:
    print(f'O valor 3 foi digitado na posição {value.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ',end='')
for n in value:
    if n % 2 == 0:
        print(n, end=' ')
