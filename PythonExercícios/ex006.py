# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

from math import sqrt
print('============= DESAFIO 06 ==============')

num = int(input('Informe um número: '))

d = num * 2
t = num * 3
r = sqrt(num)

print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {}!'.format(num, d, t, r))