matriz = [[1, 20, 3],
          [40, 25, 6]]
maior = matriz[0][0]

for i in  range(2):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
print(f'Maior: {maior}')