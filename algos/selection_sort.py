def selectionSort(arr):
    for current in range(len(arr)):
        for searcher in range(len(arr) - 1):
            if arr[searcher] > arr[current]:
               arr[current],  arr[searcher] =  arr[searcher], arr[current]
    return arr

def selectionSort1(arr):
    for idx in range(len(arr)):
        min = idx
        for idx1 in range(idx+1,len(arr)):
            if arr[idx1] < arr[min]:
                min = idx1
        arr[idx], arr[min] = arr[min],  arr[idx]
    return arr

print(selectionSort([99,44,6,2,1,5,63,87,283,4,0, 3]))
print(selectionSort([13, 4, 9, 5, 3, 16, 12, 2]))