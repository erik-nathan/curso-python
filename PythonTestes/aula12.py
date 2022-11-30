nome = str(input('Qual é o seu nome? '))
if nome == 'Erik':
     print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
     print('Seu nome é bem popular no brasil')
elif nome in 'Ana Cláudia Jessíca Juliana':
     print('Belo nome feminino')
else:
     print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
