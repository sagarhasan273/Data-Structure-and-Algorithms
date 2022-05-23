def deletion_maxHeap(arr):
    arr[0] = arr[-1]
    arr.pop()

    idx = 0
    while idx < len(arr):
        l = (2 * idx) + 1
        r = (2 * idx) + 2
        if l < len(arr) and arr[l] > arr[r] and arr[idx] < arr[l]:
            arr[idx], arr[l] = arr[l], arr[idx]
            idx = l
        elif r < len(arr) and arr[l] < arr[r] and arr[idx] < arr[r]:
            arr[idx], arr[r] = arr[r], arr[idx]
            idx = r
        else:
            break
    
    return arr + ['null']


print(deletion_maxHeap([50, 30, 20, 15, 10, 8, 16]))
        
        