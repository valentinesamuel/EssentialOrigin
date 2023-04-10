def binary_search(arr, target):
	"""Binary search only requires O(log n) time
 	:param arr: list to search
	:param target: item to search for
	:return: the position of the number in the array or -1
 """
	first = 0
	last = len(arr) - 1

	while (first <= last):
		middle = (first + last) // 2
		if (arr[middle] == target):
			return middle
		elif(arr[middle] < target):
			first = middle + 1
		else:
			last = middle - 1
	return (-1)
	
array = [0, 2, 3, 4,10, 40]

print(binary_search(array, 4))