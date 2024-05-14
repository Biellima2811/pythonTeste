# Inicializa um vetor vazio para armazenar os números inseridos pelo usuário
vetor = []

# Pede ao usuário para inserir a quantidade de números que deseja adicionar ao vetor
x = int(input('Quantos numeros deseja inserir ?: '))

# Loop para receber os números digitados pelo usuário e adicioná-los ao vetor
for i in range(x):
    num = int(input(f'Insira o {i+1}º valor: '))  # Solicita ao usuário inserir o número
    vetor.append(num)  # Adiciona o número ao vetor

# Inicializa as variáveis para armazenar o maior e o menor número no vetor
maior = vetor[0]  # Inicializa a variável 'maior' com o primeiro elemento do vetor
menor = vetor[0]  # Inicializa a variável 'menor' com o primeiro elemento do vetor

# Verifica os valores no vetor para determinar o maior e o menor número
for num in vetor:
    if num > maior:  # Verifica se o número atual é maior que 'maior'
        maior = num  # Se sim, atualiza o valor de 'maior'
    if num < menor:  # Verifica se o número atual é menor que 'menor'
        menor = num  # Se sim, atualiza o valor de 'menor'

# Exibe o maior e o menor número, além dos números digitados pelo usuário
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')
print(f'Numeros digitados: {vetor}')