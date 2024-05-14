# Vetor de exemplo
vetor = [2, 1, 3, 5, 4]

# Percorre o vetor
for i in range(len(vetor)):
    # Percorre o vetor a partir do próximo elemento após o atual
    for j in range(i + 1, len(vetor)):
        # Verifica se o elemento atual é maior que o próximo elemento
        if vetor[i] > vetor[j]:
            # Se sim, troca os elementos de posição
            organiza = vetor[i]    # Salva o valor atual em uma variável temporária
            vetor[i] = vetor[j]    # Substitui o valor atual pelo próximo valor
            vetor[j] = organiza    # Substitui o próximo valor pelo valor temporário (anterior)

# Imprime o vetor ordenado
print(vetor)
