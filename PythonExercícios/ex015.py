# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

print('============= DESAFIO 15 - Aluguel de Carros  ==============')
dias = int(input('Informe os dias alugados: '))
km = int(input('Informe os KM rodados: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
