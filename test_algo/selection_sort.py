def selectionSort(arr):
    for current in range(len(arr)):
        for searcher in range(len(arr) - 1):
            if arr[searcher] > arr[current]:
               arr[current],  arr[searcher] =  arr[searcher], arr[current]
    return arr

def selectionSort1(arr):
    length = len(arr)
    for i in range(length):
    # Initially, assume the first element of the unsorted part as the minimum.
        min = i
        for j in range(i+1, length):
            if arr[j] < arr[min]:
    # Update position of minimum element if a smaller element is found.
                min = j
    # Swap the minimum element with the first element of the unsorted part
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr

print(selectionSort1([99,44,6,2,1,5,63,87,283,4,0]))
print(selectionSort1([13, 4, 9, 5, 3, 16, 12]))