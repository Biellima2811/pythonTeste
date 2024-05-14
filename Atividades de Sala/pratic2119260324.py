vetor = [1, 2, 3, 2, 4, 5, 5, 2, 7, 8, 9, 9, 12, 22, 2]
duplicados = []

for i in range(len(vetor)):
    if i not in duplicados:
        duplicados.append(i)
print(f'Vetor Original: {vetor}')
print(f'Vetor sem elemetos duplicados: {duplicados}')