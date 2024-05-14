notas = []

for i in range(3):
    nota = float(input(f'Digite a {i + 1}º nota: '))
    notas.append(nota)

maior = max(notas)
menor = min(notas)

print(f'A maior nota: {maior}')
print(f'A menor nota: {menor}')