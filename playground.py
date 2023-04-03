def insertionSort(arr):
    for idx1 in range(1,len(arr)):
        traverser = idx1
        while traverser > 0 and arr[traverser-1] > arr[traverser]:
            arr[traverser], arr[traverser - 1] = arr[traverser - 1], arr[traverser]
            traverser -= 1
    return arr


print(insertionSort([99,44,6,2,1,5,63,87,283,4,0]))
print(insertionSort([13, 4, 9, 5, 3, 16, 12]))