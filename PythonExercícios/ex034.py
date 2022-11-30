# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('============= DESAFIO 34 - Aumentos múltiplos ==============')
salario = float(input('Informe o salário: '))
if salario > 1250.00:
    aumento1 = 1250 * 0.10
    print('Você recebeu um aumento de 10% ficando com um salário de {}'.format(1250 + aumento1))
else:
    aumento2 = 1250 * 0.15
    print('você recebeu um aumento de 15% ficando com um salário de {}'.format(1250 + aumento2))
