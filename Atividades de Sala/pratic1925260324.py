#Questão 1
vetor = [12, 13, 14, 15, 16, 25]
media = 0

for i in range(len(vetor)):
    media += vetor[i]

media = media / len(vetor)
print('A media eh : {:.2f}'.format(media))