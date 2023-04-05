def quickSort(arr, left, right):
    if len(arr) <= 1:
        return arr
    
    if left < right:
        partition_idx = partition(arr, left, right)
        left = quickSort(arr, left, partition_idx-1)
        right = quickSort(arr, partition_idx+1, right)

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    part_at = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[part_at], arr[j] = arr[j], arr[part_at]
            part_at += 1
    arr[part_at], arr[right] = arr[right], arr[part_at]
    return part_at


unsorted_arr = [7,2,1,8,6,3,5,4]
unsorted_arr1 = [22,11,88,66,55,77,33,44]
unsorted_arr2 = [7,6,10,5,9,2,1,15,7]
print(quickSort(unsorted_arr,0,len(unsorted_arr)-1))