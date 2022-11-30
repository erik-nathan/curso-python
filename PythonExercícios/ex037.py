''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.)'''

print('============= DESAFIO 37 - Conversor de Bases Numéricas ==============')
number = int(input('Informe um número para conversão: '))
print('=='*24)
print('[1] BINÁRIO | [2] OCTAL | [3] HEXADECIMAL')
option = int(input('Escolha um número: '))
print('=='*24)

if option == 1:
    print('O valor {} convertido para Binário é {}: '.format(number, bin(option)))
elif option == 2:
    print('O valor {} convertido para Octal é {}: '.format(number, oct(option)))
else:
    print('O valor {} convertido para Binário é {}: '.format(number, hex(option)))
