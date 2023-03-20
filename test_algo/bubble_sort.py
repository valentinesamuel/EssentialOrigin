numbers = [99,46,6,2,1,5,63,87,283,4,0]

def bubbleSort(array):
    for idx1 in range(len(array)):
        for idx in range(len(array)-1):
            if array[idx] > array[idx+1]:
                array[idx], array[idx+1] = array[idx+1], array[idx]
    print(array)

bubbleSort(numbers)