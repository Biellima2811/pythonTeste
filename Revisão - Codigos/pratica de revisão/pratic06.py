# Inicializa um vetor vazio para armazenar os números inseridos pelo usuário
vetor = []

# Solicita ao usuário inserir a quantidade de números que deseja adicionar ao vetor
x = int(input('Quantas vezes deseja inserir numeros: '))

# Loop para receber os números digitados pelo usuário e adicioná-los ao vetor
for i in range(x):
    num = int(input(f'Insira o {i + 1}º numero: '))  # Solicita ao usuário inserir o número
    vetor.append(num)  # Adiciona o número ao vetor

# Inicializa as variáveis maior e segundo maior com o primeiro elemento do vetor
maior = vetor[0]
seg_maior = vetor[0]

# Loop para encontrar o maior número no vetor
for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]  # Atualiza o maior número encontrado

# Loop para encontrar o segundo maior número no vetor
for i in range(len(vetor)):
    if vetor[i] > seg_maior and vetor[i] < maior:
        seg_maior = vetor[i]  # Atualiza o segundo maior número encontrado

# Exibe o segundo maior número encontrado no vetor
print(f'O segundo maior numero: {seg_maior}')
