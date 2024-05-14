# Define a matriz com os valores fornecidos
matriz = [[1, 20, 3],
          [40, 25, 6]]

# Inicializa a variável 'maior' com o primeiro elemento da matriz
maior = matriz[0][0]

# Loop para percorrer todos os elementos da matriz
for i in range(2):
    for j in range(3):
        # Verifica se o elemento atual é maior que o valor atual de 'maior'
        if matriz[i][j] > maior:
            maior = matriz[i][j]  # Atualiza o valor de 'maior' se necessário

# Exibe o maior elemento encontrado na matriz
print(f'Maior: {maior}')
