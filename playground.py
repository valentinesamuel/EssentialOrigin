def insertionSort(arr):
    for idx in range(1, len(arr)):
        curr_min = idx
        while curr_min > 0 and arr[curr_min - 1] > arr[curr_min]:
            arr[curr_min], arr[curr_min - 1] = arr[curr_min - 1], arr[curr_min]
            curr_min -= 1
    return arr

def bubbleSort(arr):
    for idx1 in range(len(arr)):
        for idx2 in range(len(arr) - idx1 - 1):
            if arr[idx2] > arr[idx2+1]:
                arr[idx2], arr[idx2 + 1] = arr[idx2 + 1], arr[idx2]
    return arr

def selectionSort(arr):
    for idx1 in range(len(arr)):
        current_min = idx1
        for idx2 in range(idx1+1, len(arr)):
            if arr[idx2] < arr[current_min]:
                current_min = idx2
        arr[idx1], arr[current_min] = arr[current_min], arr[idx1]
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
    i,j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result+=left[i:]
    result+=right[j:]

    return result

print(mergeSort([99,44,6,2,1,5,63,87,283,4,0]))
print(mergeSort([13, 4, 9, 5, 3, 16, 12]))