'''Dado um vetor "V" com 20 elementos,
criar um segundo vetor chamado de "pares" somente com os elementos pares do vetor. '''
#Vetor com valores aletorios
v = [1, 3, 6, 12, 18, 23, 27, 31, 39, 0, 51, 33, 67, 99, 51, 83, 84, 223, 222]

#Vetor com valores vazios
par = []

for i in range(len(v)):
    if v[i] % 2 == 0:
        par.append(v[i])
#Exibe os valores
print('Vetor V:', v)
#Exibe o valores pares
print('Valores pares: ', par)
