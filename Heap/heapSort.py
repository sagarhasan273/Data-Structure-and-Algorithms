def heapify(p, arr, l_idx):
    l = 2*p + 1
    r = 2*p + 2
    higher = p
    if l <= l_idx and  arr[higher] < arr[l]:
        higher = l
    if r <= l_idx and arr[higher] < arr[r]:
        higher = r
    if higher != p:
        arr[p], arr[higher] = arr[higher], arr[p]
        heapify(higher, arr, l_idx)

def heapSort(arr):
    for i in range(1, len(arr)):
        arr[0], arr[-i] = arr[-i], arr[0]
        heapify(0, arr, len(arr)-i-1)
    return arr


print(heapSort([40, 30, 15, 10, 20]))
# [50, 48, 35, 36, 35, 20, 21, 10, 5, 23, 19]