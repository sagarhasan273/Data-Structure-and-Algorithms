def heapify(i, arr):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < len(arr) and arr[largest] < arr[l]:
        largest = l
    
    if r < len(arr) and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(largest, arr)

arr = [1,2,3,4,5,6]
for i in range(len(arr)-1, -1, -1):
    heapify(i, arr)
    print(arr)

print(arr)