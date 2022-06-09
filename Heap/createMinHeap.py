from math import ceil

def insertionMinHeap(arr):
    idx = len(arr) - 1
    p = idx
    while p != 0:
        idx = p
        p = ceil(p/2) - 1
        if arr[idx] < arr[p]:
            arr[idx], arr[p] = arr[p], arr[idx]

    return arr

def heapify(i, arr, lst_idx):
    l = 2*i + 1
    r = 2*i + 2
    lower = i
    if l <= lst_idx and arr[lower] > arr[l]:
        lower = l
    if r <= lst_idx and arr[lower] > arr[r]:
        lower = r

    if lower != i:
        arr[lower], arr[i] = arr[i], arr[lower]
        heapify(lower, arr, lst_idx) 

arr = [5, 4, 6, 7, 3,2, 1]
array = [5, 20, 10, 40, 30, 15]
# for i in array:
#     arr += [i]
#     print(insertionMinHeap(arr))

# array[0], array[-1] = array[-1], array[0]
# array.pop()
# print(array)
# heapify(0, array, len(array) - 1)

for i in range(len(arr), -1, -1):
    heapify(i, arr, len(arr) - 1)
print(arr)