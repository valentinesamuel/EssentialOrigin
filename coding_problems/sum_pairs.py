arr = [1, 2, 3, 9]
arr2 = [1, 2, 4, 4]
sum = 8


def bs(array, target):
    low = 0
    high = len(array) - 1

    while (low <= high):
        middle = low + (high - low) // 2
        if (array[middle] == target):
            return array[middle]
        elif (target < array[middle]):
            high = middle - 1
        else:
            low = middle + 1
    return False


def pair_sum1(array, sum):  # O(n^2)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == sum:
                return True
    return False


def pair_sum2(array, sum):  # O(n log n)
    for i in range(len(array)):
        if (array[i] + bs(array, sum - array[i]) == sum):
            return True
    return False


def pair_sum3(array, sum):  # O(n)
    hash_set = set()
    for i in range(len(array)):
        if (sum - array[i] in hash_set):
            return True
        hash_set.add(sum - array[i])
    return False


def pair_sum4(array, sum):  # O(n)
    low = 0
    high = len(array) - 1

    while (low < high):
        if (array[low] + array[high] == sum):
            return True
        low += 1
    return False
