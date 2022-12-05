# D I C I O N Á R I O S
# Tuplas () | Listas [] | Dicionários {}

# pessoas = {'nome': 'Erik', 'sexo': 'Masc', 'idade': 22}
# # del pessoas['sexo']
# pessoas['peso'] = '95.0'
# # pessoas['nome'] = 'Nathan'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# print(pessoas.items())
# print(pessoas.values())
# print(pessoas.keys())
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# brasil = []
# estado1 = {'uf': 'Pernambuco', 'sigla': 'PE'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)



estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

