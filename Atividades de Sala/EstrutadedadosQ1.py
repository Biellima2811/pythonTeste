#Made by Gabriel Levi
#vetor com 5 números
vetor = [1, 2, 3, 4, 5]

#Número a ser procurado
x = int(input('Insira um numero: '))

#Procurando o número x no vetor
if x in vetor:
    posicao = vetor.index(x)
    print(f"O número {x} está na posição {posicao}.")
else:
    print(f"O número {x} não foi encontrado. -1")
