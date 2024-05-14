import random
import time
def quick_sort(arr):
    """
    Implementação do algoritmo Quick Sort.

    O Quick Sort é um algoritmo de ordenação eficiente que utiliza a estratégia "divide and conquer"
    (dividir para conquistar). Ele escolhe um elemento como pivô e particiona o array ao redor do
    pivô, colocando elementos menores à esquerda e elementos maiores à direita do pivô. Em seguida,
    ele ordena recursivamente as sub-listas à esquerda e à direita do pivô.

    Args:
    arr (list): A lista a ser ordenada.

    Returns:
    list: A lista ordenada.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menor_pivo = [x for x in arr[1:] if x <= pivo]
        maior_pivo = [x for x in arr[1:] if x > pivo]
        return quick_sort(menor_pivo) + [pivo] + quick_sort(maior_pivo)


def merge_sort(arr):
    """
    Implementação do algoritmo Merge Sort.

    O Merge Sort é outro algoritmo de ordenação baseado em "divide and conquer".
    Ele divide a lista em duas metades, recursivamente ordena cada metade e, em
    seguida, combina as duas metades ordenadas em uma única lista ordenada.

    Args:
    arr (list): A lista a ser ordenada.

    Returns:
    None. A lista é ordenada in-place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        metade_esquerda = arr[mid:]
        metade_direita = arr[:mid]

        # Recursivamente ordena as duas metades
        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        # Copia os elementos restantes da metade esquerda (se houver)
        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        # Copia os elementos restantes da metade direita (se houver)
        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1


# Criando uma lista antes de chamar as funções de ordenação
arr_quick = [random.randint(1, 1000) for _ in range(1000)]
arr_merge = [random.randint(1, 1000) for _ in range(1000)]

# Variáveis para armazenar o tempo de cada operação
time_quick = float('inf')
time_merge = float('inf')

# Cálculo do tempo de cada operação
inicio_time = time.time()
sorted_quick = quick_sort(arr_quick)
fim_time = time.time()
time_quick = fim_time - inicio_time
print(f'Array ordenado (Quick Sort): {sorted_quick}')
print(f'Tempo de execução (Quick Sort): {time_quick:.4f}')
# ---------------------------------

inicio_time = time.time()
merge_sort(arr_merge)
fim_time = time.time()
time_merge = fim_time - inicio_time
print(f'Array ordenado (Merge Sort): {arr_merge}')
print(f'Tempo de execução (Merge Sort): {time_merge:.4f}')
# ---------------------------------
