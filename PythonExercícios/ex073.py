'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

print("="*39)
print("DESAFIO 73 - TUPLAS COM TIME DE FUTEBOL")
print("="*39)

tabela = ('Internacional', 'Atlético MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras',
            'Santos', 'Grêmio', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará',
            'Santa Cruz', 'Bahia', 'Coritiba', 'Chapecoense', 'Botafogo', 'Vasco',
            'Atlético PR', 'Goiás')

print(f'Os cincos primeiros times da tabela são:')
for c, times in enumerate(tabela[0:5]):
    print(f'{c+1} -> {times}')
print('-'*30)

print(f'Os últimos 4 times da tabela são:')
for c, times in enumerate(tabela[16:]):
    print(f'{c+17} -> {times}')
print('-'*30)

print(f'Times em ordem alfabética: ')
ordem = sorted(tabela)
for cont in range(0, len(ordem)):
    print(f'{cont+1} -> {ordem[cont]}')
print('-' * 30)

colocação = tabela.index('Chapecoense')
print(f'Posição da Chapecoense na tabela: {colocação}')
