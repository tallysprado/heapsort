def heap(arr, n, i):
    largest = i  # raiz
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)


file = open("entrada.data", "r")
array = file.read().splitlines()
arrayNumber = list(map(int, array))
print(arrayNumber)
heapSort(arrayNumber)
n = len(arrayNumber)
print("Array ordenado por HeapSort:")
for i in range(n):
    print("%d" %arrayNumber[i])

file.close()
