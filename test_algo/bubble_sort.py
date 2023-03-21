numbers = [99,46,6,2,1,5,63,87,283,4,0]

def bubbleSort(array):
    for idx1 in range(len(array)):
        for idx in range(0,len(array)-idx1-1):
            if array[idx] > array[idx+1]:
                array[idx], array[idx+1] = array[idx+1], array[idx]
    print(array)

# def selectionSort(arr):
#     for idx in range(len(arr)):
#         min = idx
#         for idx1 in range(idx+1,len(arr)):
#             if arr[idx1] < arr[min]:
#                 min = idx1
#         arr[idx], arr[min] = arr[min],  arr[idx]
#     print(arr)

bubbleSort(numbers)