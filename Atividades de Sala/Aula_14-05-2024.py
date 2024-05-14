'''
def buscaSequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1

Realiza uma busca sequencial em uma lista para encontrar a chave especificada.

    Args:
    lista (list): A lista onde a busca será realizada.
    chave (int): A chave que está sendo procurada na lista.

    Returns:
    int: O índice da primeira ocorrência da chave na lista, ou -1 se a chave não for encontrada.

lista = [1, 2, 6, 5, 9, 10]
print(buscaSequencial(lista, 5))# Nesse comando exibirá a posição do indice.
print(buscaSequencial(lista, 3))# Nesse comando exibirá a posição de -1 pois o numero não esta na lista
'''
import copy
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1

        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

#Buca Binaria

def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = fim + 1
    return -1
lista = [10,2,40,50,1,51,100,3,39,38,22]
asc_list = lista.copy()

insertionSort(asc_list) #Cria uma cópia da lista para ordenação

chave_buscar = 11 #Variavel criada para ser buscada na lista (se houver!)

#Realiza a busca binairia na lista ordenada
indice_encontrado = buscaBinaria(asc_list, chave_buscar)

if indice_encontrado != -1:
    print(f'A chave {chave_buscar} foi encontrada na posição {indice_encontrado} da lista.')
else:
    print(f'A chave {chave_buscar} não foi encontrada na lista ordenada. ')