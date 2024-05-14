# Define a matriz com os valores fornecidos
matriz = [[10, 9, 9],
          [7, 8, 9]]

# Inicializa a variável 'media' com o valor zero
media = 0

# Loop para percorrer todos os elementos da matriz
for i in range(2):
    for j in range(3):
        media += matriz[i][j]  # Adiciona o valor do elemento atual à variável 'media'

# Divide a soma de todos os elementos pelo total de elementos na matriz para calcular a média
media = media / 6

# Exibe a média calculada, formatada com duas casas decimais
print(f'A media calculada é: {media:.2f}')
