def insertionSort2(arr):
    for idx in range(1, len(arr)):
        temp = arr[idx]    
        idx2 = idx-1
        while (idx2 >= 0 and  arr[idx2] > temp):
            arr[idx2+1] = arr[idx2]
            idx2-=1
        arr[idx2+1] = temp
    return arr

def bubbleSort(arr):
    for idx in range(len(arr)):
        for idx2 in range(len(arr)-idx-1):
            if arr[idx2] > arr[idx2+1]:
                arr[idx2], arr[idx2+1] = arr[idx2+1], arr[idx2]
    return arr

def insertionSort(arr):
    for idx in range(1, len(arr)):
        currmin = idx
        while currmin > 0 and arr[currmin-1] > arr[currmin]:
            arr[currmin], arr[currmin-1] = arr[currmin-1], arr[currmin]
            currmin -=1
    return arr


def selectionSort(arr):
    for idx1 in range(len(arr)):
        min = idx1
        for idx2 in range(idx1,len(arr)):
            if arr[idx2] < arr[min]:
                min = idx2
        arr[idx1], arr[min] = arr[min], arr[idx1]
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)
    
def merge(left, right):

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
        
    return result


print(insertionSort([99,44,6,2,1,5,63,87,283,4,0]))
print(insertionSort([13, 4, 9, 5, 3, 16, 12]))