# Questão 2
vetor = [12, -1, 45, -12, 9, 2]
menor = vetor[0]
maior = vetor[0]

for i in range(len(vetor)):
    if vetor [i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print('Maior é : {}'.format(maior))
print('Menor é : {}'.format(menor))