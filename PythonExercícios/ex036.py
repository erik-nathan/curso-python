''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('============= DESAFIO 36 - Aprovando Empréstimo ==============')
valueHome = float(input('Informe o valor da casa: R$'))
buyerSalary = float(input('Informe o salário do comprador: R$'))
howOld = int(input('Informe em quantos anos ele vai pagar: '))

preSalary = valueHome / (howOld * 12)

if preSalary < buyerSalary * 30 / 100:
    print('FINANCIAMENTO ACEITO!!!\n- A prestação será de R${:.2f} por mês durante {} Anos.'.format(preSalary, howOld))
else:
    print('FINANCIAMENTO NEGADO!!!\n- SALÁRIO INSUFICIENTE.')

