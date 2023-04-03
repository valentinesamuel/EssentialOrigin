def partition1(arr, high, low=0):
    if not arr and not high:
        return 'No array and no upperbound'


    pivot = arr[high]
    partion_at = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[partion_at], arr[j] = arr[j], arr[partion_at]
            partion_at += 1
    arr[partion_at], arr[high] = arr[high], arr[partion_at]  
    return partion_at

def partition(array, low, high):
            pivot = array[high]
            partat = low
            for i in range(low, high):
                if array[i] <= pivot:
                    array[partat], array[i] = array[i], array[partat]
                    partat = partat + 1

            array[partat], array[high] = array[high], array[partat]
            return partat