'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais..'''

print("="*37)
print("DESAFIO 77 - CONTANTO VOGAIS EM TUPLA")
print("="*37)

vogais = 'aeiou'
palavras = ('carro', 'moto', 'arruda', 'bicicleta', 'computador', 'celular')
for p in palavras:
    print(f'\nVogais da palavra {p.upper()} -> ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')
