def quickSort(arr, low, high):
    if low < high:
        partition_idx = partition(arr, low, high)
        quickSort(arr, low, partition_idx-1)
        quickSort(arr, partition_idx+1, high)
    return arr

def partition(arr, low, high):
    if not arr and not high:
        return 'No array and no upperbound'

    pivot = arr[high]
    partition_at = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[partition_at], arr[j] = arr[j], arr[partition_at]
            partition_at += 1
    
    arr[partition_at], arr[high] = arr[high], arr[partition_at]
    return partition_at


unsorted_arr = [7,2,1,8,6,3,5,4]
unsorted_arr1 = [22,11,88,66,55,77,33,44]
unsorted_arr2 = [7,6,10,5,9,2,1,15,7]
print(quickSort(unsorted_arr,0,len(unsorted_arr)-1))