'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

print("="*30)
print("DESAFIO 97 - Um print especial")
print("="*30)

def escreva(text):
    tam = len(text) + 4
    print('=' *tam)
    print(f'  {text}')
    print('=' *tam)

t = str(input('Digite um texto qualquer: '))
escreva(t)
