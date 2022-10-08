array = [2, 5, 1, 2, 3, 5, 1, 2, 4] # return 2
# [2,1,1,2,3,5,1,2,4] # return 1
# [2,3,4,5] # return none

def containsDuplicate(arr):
	register = {}
	hasDuplicate = None
	if (not isinstance(arr, list) or len(arr) == 0):
		raise ValueError("List is invalid, not provided or empty")
	
	for ele in arr:
		if ele in register:
			hasDuplicate = True
			break
		else:
			register[ele] = 1
		hasDuplicate = False
	
	return hasDuplicate

print(containsDuplicate(True))