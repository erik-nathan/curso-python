# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print("="*35)
print("DESAFIO 53 - DETECTOR DE PALÍNDROMO")
print("="*35)

#strip() : retira os espaços da frase | upper() : todos caracteres em maiúsculos
frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
