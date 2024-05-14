'''Crie um vetor de 1000 elementos desordenados
    * -> Bubble, Selection, Insertion sort e calcule o tempo de cada um, ex: algoritimo + tempo
'''
import random
import time

def Bubble_sort(arr):
    """
    Ordena um array usando o algoritmo Bubble Sort.

    Args:
    arr (list): O array a ser ordenado.

    Returns:
    None. A função modifica o array fornecido, ordenando-o em ordem crescente.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def Selection_sort(arr):
    """
    Ordena um array usando o algoritmo Selection Sort.

    Args:
    arr (list): O array a ser ordenado.

    Returns:
    None. A função modifica o array fornecido, ordenando-o em ordem crescente.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def Insertion_sort(arr):
    """
    Ordena um array usando o algoritmo Insertion Sort.

    Args:
    arr (list): O array a ser ordenado.

    Returns:
    None. A função modifica o array fornecido, ordenando-o em ordem crescente.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Cria um vetor de 5000 elementos desordenados com números aleatórios entre 1 e 5000
arr = [random.randint(1, 1000) for _ in range(1000)]

# Faz uma cópia do vetor original para cada algoritmo de ordenação
arr_bubble = arr.copy()
arr_selection = arr.copy()
arr_insertion = arr.copy()

# Variáveis para armazenar os tempos de execução dos algoritmos
time_bubble = float('inf')
time_selection = float('inf')
time_insertion = float('inf')

# Medição do tempo de execução do Bubble Sort
inicio_time = time.time()
Bubble_sort(arr_bubble)
fim_time = time.time()
time_bubble = fim_time - inicio_time

# Medição do tempo de execução do Selection Sort
inicio_time = time.time()
Selection_sort(arr_selection)
fim_time = time.time()
time_selection = fim_time - inicio_time

# Medição do tempo de execução do Insertion Sort
inicio_time = time.time()
Insertion_sort(arr_insertion)
fim_time = time.time()
time_insertion = fim_time - inicio_time

# Identifica o algoritmo mais rápido
fastest_algorithm = min(time_bubble, time_selection, time_insertion)

# Exibe os primeiros elementos dos arrays ordenados e os tempos de execução
print('Primeiros Elementos dos arrays ordenados:')
print(f'Bubble Sort: {arr_bubble}...')
print(f'Tempo: {time_bubble:.4f} segundos')
print(f'Selection Sort: {arr_selection}...')
print(f'Tempo: {time_selection:.4f} segundos')
print(f'Insertion Sort: {arr_insertion}...')
print(f'Tempo: {time_insertion:.4f} segundos')

# Exibe o algoritmo mais rápido
print('\tMelhor Caso:')
if fastest_algorithm == time_bubble:
    print(f'\tBubble Sort foi o mais rápido com tempo de execução: {fastest_algorithm:.4f} segundos.')
elif fastest_algorithm == time_selection:
    print(f'\tSelection Sort foi o mais rápido com tempo de execução: {fastest_algorithm:.4f} segundos.')
else:
    print(f'\tInsertion Sort foi o mais rápido com tempo de execução: {fastest_algorithm:.4f} segundos.')
