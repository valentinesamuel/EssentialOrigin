def merge_sorted_arrays(array1, array2):
    flag = 0
    sorted_array = []
    first_array_index = 0
    second_array_index = 0

    while not (first_array_index >= len(array1) or second_array_index >= len(array2)): # so long as we haven't gotten to the end of either array
        if array1[first_array_index] < array2[second_array_index]: # check which array item is smaller and add it to sorted array
            sorted_array.append(array1[first_array_index])
            first_array_index+=1
        else:
            sorted_array.append(array2[second_array_index])
            second_array_index+=1

        if first_array_index == len(array1): # If the first araay finishes before the second one
            flag = 1


    if flag == 1:
        for item in array2[second_array_index:]:
            sorted_array.append(item)
    else:
        for item in array1[first_array_index:]:
            sorted_array.append(item)
    return sorted_array



print(merge_sorted_arrays([1,3,5,7,9,11,13], [2,4,6,8]))