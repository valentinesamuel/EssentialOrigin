def reverse_string1(string):
	if (not string and len(string) < 2):
		return
	return ''.join(string[::-1])

def reverse_string2(string):
	string = list(string)
	low = 0
	high = len(string) - 1

	while (low <= high):
		string[low], string[high] = string[high], string[low]
		low+=1
		high-=1
	return ''.join(string)

print(reverse_string2("hello"))