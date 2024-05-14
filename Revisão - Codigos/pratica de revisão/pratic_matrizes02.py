# Define as matrizes originais
matriz = [[1, 20, 3],
          [40, 45, 6]]

matriz_2 = [[1, 20, 3],
            [4, 4, 9]]

# Inicializa uma matriz vazia para armazenar o resultado da soma das duas matrizes
matriz_limp = [[0, 0, 0],
               [0, 0, 0]]

# Loop para percorrer todas as posições das matrizes
for i in range(2):
    for j in range(3):
        # Soma os elementos correspondentes das duas matrizes e atribui o resultado à matriz resultante
        matriz_limp[i][j] = matriz[i][j] + matriz_2[i][j]

# Exibe a matriz resultante
print(f'Resultado: {matriz_limp}')
