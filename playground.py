def insertionSort2(arr):
    for idx in range(1, len(arr)):
        temp = arr[idx]    
        idx2 = idx-1
        while (idx2 >= 0 and  arr[idx2] > temp):
            arr[idx2+1] = arr[idx2]
            idx2-=1
        arr[idx2+1] = temp
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

print(mergeSort([99,44,6,2,1,5,63,87,283,4,0]))
print(mergeSort([13, 4, 9, 5, 3, 16, 12]))