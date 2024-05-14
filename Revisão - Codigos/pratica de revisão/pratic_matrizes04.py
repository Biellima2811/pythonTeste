# Inicializa uma lista vazia para armazenar as notas dos alunos
alunos = []

# Loop para inserir as notas dos 5 alunos
for i in range(5):
    nota = float(input('Insira a nota do aluno: '))  # Solicita ao usuário inserir a nota do aluno
    alunos.append(nota)  # Adiciona a nota à lista de notas dos alunos

# Calcula a média da turma
media = sum(alunos) / len(alunos)

# Encontra a maior e a menor nota da turma
maior = max(alunos)
menor = min(alunos)

# Exibe a média da turma, a maior e a menor nota, formatadas com duas casas decimais
print(f'Media da turma: {media:.2f}')
print(f'Maior nota: {maior:.2f}')
print(f'Menor nota: {menor:.2f}')
