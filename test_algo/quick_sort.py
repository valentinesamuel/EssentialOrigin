def quickSort(arr, left, right):
    if left < right:
        partition_idx = partition(arr, left, right)
        left = quickSort(arr, left, partition_idx-1)
        right = quickSort(arr, partition_idx+1, right)

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    partion_at = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[partion_at], arr[j] = arr[j], arr[partion_at]
            partion_at += 1
    
    arr[partion_at], arr[right] = arr[right], arr[partion_at]
    return partion_at



unsorted_arr = [7,2,1,8,6,3,5,4]
unsorted_arr1 = [22,11,88,66,55,77,33,44]
unsorted_arr2 = [7,6,10,5,9,2,1,15,7]
print(quickSort(unsorted_arr2,0,len(unsorted_arr2)-1))