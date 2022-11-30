'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

print('============= DESAFIO 38- Comparando números ==============')
valueOne = int(input('Informe o primeiro número: '))
valueTwo = int(input('Informe o segundo número: '))
print('=='*24)

if valueOne > valueTwo:
    print('O PRIMEIRO VALOR E MAIOR')
elif valueTwo > valueOne:
    print('O SEGUNDO VALOR É MAIOR')
elif valueTwo == valueOne:
    print('NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS')