'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('============= DESAFIO 44 - Gerenciador de Pagamentos ==============')
valueProd = float(input('Informe o valor do produto: R$'))
print('Á VISTA [1] | DÉBITO [2] | 2X NO CARTÃO [3] | 3X OU MAIS NO CARTÃO [4]')
condPag = int(input('Escolha a opção de pagamanto: '))
print('=='*24)

if condPag == 1:
    print('Você recebeu um desconto de 10%, ficando com o valor de: R${}'.format(valueProd - (valueProd * (10 / 100))))
elif condPag == 2:
    print('Você recebeu um desconto de 5%, ficando com o valor de: R${}'.format(valueProd - (valueProd * (5 / 100))))
elif condPag == 3:
    print('Você pagará o valor formal: R${}'.format(valueProd))
elif condPag == 4:
    print('Você pagará 20% de juros, ficando com o valor de: R${}'.format(valueProd + (valueProd * (20 / 100))))
else:
    print('NÃO EXISTE ESSA FORMA DE PAGAMENTO')


