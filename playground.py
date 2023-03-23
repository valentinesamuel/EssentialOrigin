def selectionSort(arr):
    for idx1 in range(len(arr)):
        min = idx1
        for idx2 in range(idx1+1, len(arr)):
            if arr[idx2] < arr[min]:
               min = idx2
        arr[idx1], arr[min] = arr[min], arr[idx1]
    return arr
        




def bubbleSort(arr):
    for idx1 in range(len(arr)):
      for idx2 in range(len(arr)-idx1-1):
         if arr[idx2] > arr[idx2+1]:
            arr[idx2+1], arr[idx2] = arr[idx2], arr[idx2+1]
    return arr

    

print(selectionSort([99,44,6,2,1,5,63,87,283,4,0]))
print(selectionSort([13, 4, 9, 5, 3, 16, 12]))