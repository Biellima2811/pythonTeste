# Inicializa uma lista vazia para armazenar as notas inseridas pelo usuário
notas = []

# Loop para solicitar ao usuário inserir as notas
for i in range(3):
    num = float(input(f'Insira a {i + 1}º nota: '))  # Solicita ao usuário inserir a nota
    notas.append(num)  # Adiciona a nota à lista de notas

# Encontra a maior e a menor nota na lista 'notas'
maior = max(notas)  # Encontra a maior nota na lista 'notas'
menor = min(notas)  # Encontra a menor nota na lista 'notas'

# Exibe a maior e a menor nota encontradas, formatadas com duas casas decimais
print(f'A maior nota: {maior:.2f}')
print(f'A menor nota: {menor:.2f}')
