# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E
# MILÍMETROS.

print('============= DESAFIO 08 ==============')

n = float(input('Informe um valor em metros: '))

cen = n * 100
mil = n * 1000

print("{} metros, {} centímetros, {} milímetros".format(n, cen, mil))
