vetor = [1, 2, 3, 4, 5, 4, 6, 7, 4, 8, 9, 4]
num = int(input('Insira um numero de 1 a 10: '))
cont = 0
for i in vetor:
    if i == num:
        cont += 1

print(f'O numero {num}, aparece {cont} vezes')