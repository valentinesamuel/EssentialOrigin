def selectionSort(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i + 1, len(arr)):
			if arr[min] > arr[j]:
				min = j
		arr[min], arr[i] = arr[i], arr[min]
	return arr


def insertionSort(arr):
	for i in range(1, len(arr)):
		min = i
		while min > 0 and arr[min - 1] > arr[min]:
			arr[min], arr[min - 1] = arr[min - 1], arr[min]
			min -= 1
	return arr


def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr


lst = [2, 4, 7, 2, 6, 8, 12, 1, 0]
print(insertionSort(lst))
print(selectionSort(lst))
print(bubbleSort(lst))
