#Questão 6
vetor = [12, 12, 10, 20, 24, 45, 9, 2]
pares = []
soma = 0

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
        soma = soma + vetor[i]
print(f'Os pares são : {pares}')
print(f'A soma dos pares eh: {soma}')
