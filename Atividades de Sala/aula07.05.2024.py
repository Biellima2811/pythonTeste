def insertion_sort(arr):
    n = len(arr)

    #Pecorre todos os elementos do array
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        #Move os elementos do arr[0...i-1], que são maiores que key
        #Para uma posição à frente de sua posição atual

        while j <= 0 and key > arr[j]:
            arr[j +1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

arr = [65,25, 12,22,11]
insertion_sort(arr)

print('Array Ordenado')
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")