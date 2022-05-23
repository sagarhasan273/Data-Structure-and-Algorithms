from math import ceil


def createHeap(arr):
    for i in range(len(arr)):
        idx = i
        while idx != 0:
            id = idx
            idx = ceil(idx/2) - 1
            if arr[id] > arr[idx]:
                arr[id], arr[idx] = arr[idx], arr[id]
    print(arr)


createHeap([10, 20, 15, 30, 40])