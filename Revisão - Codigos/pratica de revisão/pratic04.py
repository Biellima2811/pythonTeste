# Inicializa um vetor vazio para armazenar os números inseridos pelo usuário
vetor = []

# Define o elemento a ser contado no vetor
elemento = 2

# Solicita ao usuário inserir a quantidade de números desejada
x = int(input('Insira quantos números deseja inserir: '))

# Inicializa um contador para contar as ocorrências do elemento no vetor
cont = 0

# Loop para receber os números digitados pelo usuário e adicioná-los ao vetor
for i in range(x):
    num = int(input(f'Insira o {i + 1}º número de 1 a 10: '))  # Solicita ao usuário inserir o número
    vetor.append(num)  # Adiciona o número ao vetor
    if num == elemento:  # Verifica se o número inserido é igual ao elemento desejado
        cont += 1  # Se sim, incrementa o contador

# Exibe o resultado do número de ocorrências do elemento no vetor
print(f'O número {elemento} apareceu {cont} vezes.')