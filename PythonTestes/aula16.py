# TUPLAS SÃO IMUTÁVEIS

pessoa = ('Erik', 39, 'M', 99.880)
# del(pessoa)
print(pessoa)

# a = 2, 5, 4
# b = 5, 8, 1, 2
# c = a + b
# #print(c)
# print(c.index(2))

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# print(sorted(lanche))

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
