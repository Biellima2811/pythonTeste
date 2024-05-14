# Solicita ao usuário inserir o número de elementos desejados no vetor
n = int(input('Quantos numeros deseja inserir ?: '))

# Inicializa um vetor vazio para armazenar os valores inseridos pelo usuário
vetor = []''

# Loop para receber os valores do usuário e adicioná-los ao vetor
for i in range(n):
    valor = float(input('Digite o {}º valor: '.format(i + 1)))  # Solicita ao usuário inserir o valor
    vetor.append(valor)  # Adiciona o valor ao vetor

# Inicializa a variável para armazenar a soma dos valores
soma = 0

# Calcula a soma de todos os valores no vetor
for valor in vetor:
    soma += valor

# Calcula a média dividindo a soma pelo número de elementos no vetor
media = soma / len(vetor)

# Exibe a média dos valores no vetor
print('A media dos valores no vetor é: {}'.format(media))
