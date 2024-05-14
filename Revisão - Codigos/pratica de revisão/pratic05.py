# Inicializa um vetor vazio para armazenar os números inseridos pelo usuário
vetor = []

# Pede ao usuário inserir a quantidade de números desejada
x = int(input('Quantas vezes deseja inserir número?: '))

# Inicializa a variável para armazenar a soma dos números pares
soma = 0

# Loop para receber os números digitados pelo usuário e adicioná-los ao vetor
for i in range(x):
    num = float(input(f'Insira o {i + 1}º valor: '))  # Solicita ao usuário inserir o número
    vetor.append(num)  # Adiciona o número ao vetor

    # Verifica se o número inserido é par
    if num % 2 == 0:
        soma += num  # Se sim, adiciona o número à soma

# Exibe o resultado da soma de todos os elementos pares no vetor
print(f'A soma de todos os elementos pares no vetor é: {soma}')
