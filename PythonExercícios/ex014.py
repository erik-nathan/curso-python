# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('============= DESAFIO 14 - Conversor de Temperaturas  ==============')

cel = float(input('Informe a temperatura em Celsius: '))

f = (cel * 1.8) + 32

print('A temperatura em Celsius {} em Fahrenheit é {}'.format(cel, f))
