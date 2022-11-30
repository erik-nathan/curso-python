'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

print('============= DESAFIO 46 - Contagem Regressiva ==============')
from time import sleep
print('- - - C O N T A G E M  R E G R E S S I V A - - -')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(' = = = F E L I Z  A N O  N O V O = = =')
