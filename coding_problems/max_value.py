def max_value(nums):
	"""
 	Receives an arry and search for the maximum value
	Arguments:
 		array: an array of integers
	"""
	max_value = float('-inf')
	for i in range(len(nums)):
		if nums[i] > max_value:
			max_value = nums[i]
	return max_value
