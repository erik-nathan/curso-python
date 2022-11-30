'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500'''

print('============= DESAFIO 48 - Soma ímpares múltiplos de três ==============')
m = 0
for c in range(1, 500):
    if c % 3 == 0:
        m += c
print(m)
