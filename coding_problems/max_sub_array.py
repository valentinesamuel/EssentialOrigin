"""Given an integer array nums, 
find the contiguous subarray 
(containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
def max_sub_array(arr):
	max_sum = arr[0]
	current_sum = max_sum
	for ele in arr:
		current_sum = max(current_sum + ele, ele)
		max_sum = max(max_sum, current_sum)
	return max_sum

def max_sub_array2(arr):
	totalmax = 0
	currentmax = arr[0]
	for ele in arr:
		currentmax = currentmax + ele
		if currentmax < ele:
			currentmax = ele
		if totalmax < currentmax:
			totalmax = currentmax
	return totalmax

def max_sub_array3(arr):
	current_sum = global_sum = arr[0]
	for ele in arr:
		current_sum = max(ele, current_sum + ele)
		if current_sum > global_sum:
			global_sum = current_sum
	return global_sum

	
print(max_sub_array2([-2,1,-3,4,-1,2,1,-5,4])) 