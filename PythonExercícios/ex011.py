# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LO,
# SABENDO QUE CADA LITRO DE TINRA, PINTA UMA ÁREA DE 2M^2

print('============= DESAFIO 11 ==============')

l = float(input('Informe a largura: '))
a = float(input('Informe a altura: '))

area = l * a
tinta = area / 2

print('Para pintar uma area de {} é necessário {} litros de tinta'.format(area, tinta))
