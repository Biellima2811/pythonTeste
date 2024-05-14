# Questão 5
vetor = [1,2,3,2,4,5,5,2,7,8,9,9,12,22,2]

element = 2
repet = 0
for i in vetor:
    if i == element:
        repet += 1
print('O vetor selecionar foi: {}'.format(element))
print('O elemento {} ocorre {} vezes no vetor'.format(element, repet))