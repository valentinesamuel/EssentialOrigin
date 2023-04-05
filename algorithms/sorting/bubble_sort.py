def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr) - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr


# def bubbleSort2(arr):
# 	for i in range(len(arr)):
# 		for j in range(len(arr) - i - 1):
# 			if arr[j] > arr[j+1]:
# 				arr[j], arr[j+1] = arr[j+1], arr[j]
# 	return arr

# def bubbleSort3(arr):
# 	for i in range(len(arr)):
# 		flag = 0
# 		for j in range(len(arr) - i - 1):
# 			if arr[j] > arr[j+1]:
# 				arr[j], arr[j+1] = arr[j+1], arr[j]
# 				flag = 1
# 		if(flag == 0):
# 			break
# 	return arr

lst = [2, 4, 7, 2, 6, 8, 12, 1, 0]
print(bubbleSort(lst))
