# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

print("="*33)
print("DESAFIO 51 - PROGRESSÃO DE UMA PA")
print("="*33)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + 10 * r

for c in range(p, d, r):
    print(c, end=' -> ')
print('FIM')