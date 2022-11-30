# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('============= DESAFIO 49 - Tabuada V.0.2 ==============')

n = int(input('Informe um número: '))
print("TABUADA DE {}".format(n))
for c in range(1, 11):
    print("{} x {}: {}".format(n, c, n * c))
print("FIM DA TABUADA")
