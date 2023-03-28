def insertionSort(arr):
    for idx in range(1, len(arr)):
        currSmallest = idx
        while currSmallest > 0 and arr[currSmallest-1] > arr[currSmallest]:
            arr[currSmallest], arr[currSmallest - 1] = arr[currSmallest-1], arr[currSmallest]
            currSmallest -= 1
    return arr

print(insertionSort([99,44,6,2,1,5,63,87,283,4,0]))
print(insertionSort([13, 4, 9, 5, 3, 16, 12]))