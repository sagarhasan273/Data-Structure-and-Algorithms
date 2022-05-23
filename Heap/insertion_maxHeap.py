from math import ceil


def insertion_heap(arr, key):
    arr += [key]
    indx = len(arr) - 1
    while indx != 0:
        idx = ceil(indx/2) - 1
        arr[indx], arr[idx] = arr[idx], arr[indx]
        indx = idx
    
    return arr


print(insertion_heap([50,30, 20, 15, 10, 8, 16], 60))