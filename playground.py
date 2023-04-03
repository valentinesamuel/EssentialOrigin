def insertionSort(arr):
    for idx1 in range(1,len(arr)):
        traverser = idx1
        while traverser > 0 and arr[traverser-1] > arr[traverser]:
            arr[traverser], arr[traverser - 1] = arr[traverser - 1], arr[traverser]
            traverser -= 1
    return arr

def selectionSort(arr):
    for idx1 in range(len(arr)):
        curr_min = idx1
        for idx2 in range(idx1+1, len(arr)):
            if arr[idx2] < arr[curr_min]:
                curr_min = idx2
        arr[idx1], arr[curr_min] = arr[curr_min], arr[idx1] 
    return arr


print(selectionSort([99,44,6,2,1,5,63,87,283,4,0]))
print(selectionSort([13, 4, 9, 5, 3, 16, 12]))