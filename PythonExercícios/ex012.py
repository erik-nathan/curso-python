# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO,
# COM 5% DE DESCONTO.

print('============= DESAFIO 12 ==============')

n = float(input('Informe o preço do produto: '))

newValue = (n * 5) / 100
valueProd = n - newValue

print('O novo preço com desconto de 5% é R${}'.format(valueProd))
