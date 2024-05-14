vetor = [10, 5, 8, 20, 15, 12]
maior = vetor[0]
segundo_maior = vetor[0]

for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
for i in range(len(vetor)):
    if vetor[i] > segundo_maior and vetor[i] < maior:
        segundo_maior = vetor[i]
print(f'O segundo maior eh: {segundo_maior}')

'''vetor = [10, 5, 8, 20, 15, 12]
Inicializa um codição o maior e o segundo maior com os primeiros dois elementos do vetor.
if vetor[0] > vetor[1]:
    maior = vetor[0]
    segundo_maior = vetor[1]
else:
    maior = vetor[1]
    segundo_maior[0]
#Pecorre o vetor para encontrar o maior e o segundo maior
for i in range(2,len(vetor)):
    if vetor[i] > maior:
        segundo_maior = maior
        maior = vetor[i]
    elif vetor[i] > segundo_maior and vetor[i] != maior:
        segundo_maior = vetor[i]
print(f'O segundo maior no vetor é: {segundo_maior}')'''