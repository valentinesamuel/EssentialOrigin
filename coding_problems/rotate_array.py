def rotateArray(array, displacement):
	displacement = displacement % len(array)
	reverse(array, 0, len(array) - 1)
	reverse(array, 0, displacement - 1)
	reverse(array, displacement, len(array) - 1)
	return array

def reverse(arr, start, end):
	while(start < end):
		arr[start], arr[end] = arr[end], arr[start]
		start+=1
		end-=1
		
print(rotateArray([1,2,3,4,5,6,7], 3))