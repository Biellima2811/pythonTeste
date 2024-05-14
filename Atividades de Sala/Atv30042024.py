import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f'I = {i}')
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
    print(arr)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(arr)
#cria um array com 1000 elementos aleatorios
arr = [random.randint(1, 1000) for _ in range(1000)]

#Realiza a copia de array original para os algoritimos de ordenação
bubble_arr = arr.copy()
selection_arr = arr.copy()

#Medição de tempo para o Bubble
inicio_tempo = time.time()
bubble_sort(bubble_arr)
fim_tempo = time.time()
print(f'O tempo de execução do Bubble sort: {fim_tempo - inicio_tempo:.4f} segundos')

#Medição do tempo para o Selection
inicio_tempo = time.time()
selection_sort(selection_arr)
fim_tempo = time.time()
print(f'O tempo de execução do Selection sort: {fim_tempo - inicio_tempo:.4f} segundos')
