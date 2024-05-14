matriz01 = [[1, 20, 3],
            [40, 45, 6]]

matriz02 = [[1, 20, 3],
            [4, 4, 9]]

matriz03 = [[0, 0, 0],
            [0, 0, 0]]

for i in range(2):
    for j in range(3):
        matriz03[i][j] = matriz01[i][j] + matriz02[i][j]
print(matriz03)