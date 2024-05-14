vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for i in vetor:
    if i % 2 == 0: # verifica se o elemento é par
        soma = soma + i
print(f'A soma de todos os elementos pares do vetor eh : {soma}')