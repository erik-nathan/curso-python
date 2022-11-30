# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO,
# COM 15% DE AUMENTO.

print('============= DESAFIO 13 - Reajuste Salarial ==============')

s = float(input('Informe o salário: '))

newWage = s + (s * 15 / 100)

print('O novo salário com aumento de 15% é: {}'.format(newWage))
