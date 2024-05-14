# Inicializa três vetores vazios para armazenar os números inseridos, seus cubos e seus quadrados
vetor = []       # Armazena os números inseridos
cubo = []        # Armazena os cubos dos números inseridos
quadrado = []    # Armazena os quadrados dos números inseridos

# Solicita ao usuário inserir a quantidade de números que deseja adicionar ao vetor
x = int(input('Quantos numeros deseja inserir no vetor ?: '))

# Loop para inserir os números no vetor e calcular seus cubos e quadrados
for i in range(x):
    num = int(input('Insira o {}º valor: '.format(i + 1)))  # Solicita ao usuário inserir o número
    vetor.append(num)        # Adiciona o número ao vetor
    cubo.append(num ** 2)    # Calcula o cubo do número e adiciona ao vetor cubo
    quadrado.append(num ** 3)  # Calcula o quadrado do número e adiciona ao vetor quadrado

# Exibe os números inseridos no vetor, seus cubos e seus quadrados
print(f'Numeros inseridos no vetor: {vetor}')
print(f'Numeros ao cubo dos inseridos: {cubo}')
print(f'Numeros ao quadrado dos inseridos: {quadrado}')