def moving_zeros(array):
    """move all zeros to the end of the array while keeping the order. Modify the array in place"""
    leftPointer = 0
    for rightPointer in range(len(array)):
        if (array[rightPointer] != 0):
            array[leftPointer], array[rightPointer] = array[
                rightPointer], array[leftPointer]
            leftPointer += 1
    return (array)


print(moving_zeros([8, 0, 3, 0, 3, 6, 0, 0, 0, 12]))
