def bubble_sort(arr):
    """
    Ordena um array usando o algoritmo de classificação bolha.

    Args:
    arr (list): O array a ser ordenado.

    Returns:
    None. A função modifica o array fornecido, ordenando-o em ordem crescente.

    """
    n = len(arr)  # Calcula o comprimento do array
    # Percorre todos os elementos do array
    for i in range(n):
        print(f'i = ', i)
        for j in range(0, n-i -1):  # Percorre os elementos do array, até n-i-1
            # Troca se o elemento encontrado for maior que o próximo elemento.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
                print(arr)  # Imprime o array após cada troca
    print(arr)  # Imprime o array final após todas as trocas

    for i in range(n):
        print('i = ', i)
        for j in range (0, n-i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
    print(arr)

# Array de exemplo
arr = [10, 9, 3, 8, 4, 7, 5, 2, 6, 1]
# Chama a função bubble_sort para ordenar o array
bubble_sort(arr)