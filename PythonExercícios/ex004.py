# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES SOBRE ELE.

aux = input('Digite algo: ')

print('O tipo primitivo desse valor é {}', type(aux))
print('Só tem espaços? ', aux.isspace())
print('É um número? ', aux.isnumeric())
print('É alfabético? ', aux.isalpha())
print('É alfanumérico? ', aux.isalnum())
print('Está em maiúsculas? ', aux.isupper())
print('Está em minúsculas? ', aux.islower())
print('Está em capitalizada? ', aux.istitle())
