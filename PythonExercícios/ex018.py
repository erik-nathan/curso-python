# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
print('============= DESAFIO 18 - Seno, Cosseno e Tangente  ==============')
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, tan))
