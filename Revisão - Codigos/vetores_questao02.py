vetor = [1,2,3,4,5,6,7,8]
cubo = []
quadrado = []

for i in vetor:
    quadrado.append(i ** 2)
    cubo.append(i ** 3)
print(f'Vetor : {vetor}')
print(f'Quadrados: {quadrado}')
print(f'Cubo: {cubo}')