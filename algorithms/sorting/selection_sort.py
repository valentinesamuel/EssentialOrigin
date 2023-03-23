def selectionSort(arr):
	for current_element in range(len(arr)):
		current_minimum = current_element
		for smallest in range(current_element + 1, len(arr)):
			if arr[current_minimum] > arr[smallest]:
				current_minimum = smallest
		arr[current_element], arr[current_minimum] = arr[current_minimum], arr[
		 current_element]
	return arr


lst = [2, 4, 7, 2, 6, 8, 12, 1, 0]
print(selectionSort(lst))
