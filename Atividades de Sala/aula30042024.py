def selection_sort(arr):
    n = len(arr)

    #Percorre todos os elementos do array
    for i in range(n):
        #Encontra o indice do menor elemento restante
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Troca o menor elemento encontrado com o primeiro elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(arr)
#exibe os valores
arr = [64, 25, 12, 11, 22, 26, 28, 32, 30, 10]
print(arr)
selection_sort(arr)

print('Array ordenado')
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")