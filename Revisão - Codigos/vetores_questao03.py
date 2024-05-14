vertor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = vertor[0]
menor = vertor[0]

for i in vertor:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'Maior: {maior}')
print(f'Menor: {menor}')