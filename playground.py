def partition(arr, high, low=0):
    if not arr and not high:
        return 'No array and no upperbound'

    pivot = arr[high]
    partion_at = low
    for j in range(low, high+1):
        if arr[j] <= pivot:
            arr[partion_at], arr[j] = arr[j], arr[partion_at]
            partion_at += 1
    arr[partion_at], arr[high] = arr[high], arr[partion_at]  
    return partion_at


unsorted_arr = [7,2,1,8,6,3,5,4]
print(partition(unsorted_arr,len(unsorted_arr)-1))