n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS')


# nome = str(input('Qual é o seu nome? '))
# # if nome == 'Erik':
# #     print('Que nome lindo você tem!')
# # else:
# #     print('Seu nome é tão normal!')
# # print('Bom dia, {}!'.format(nome))