def moving_odd(prime_numbers):
	"""Moves odd numbers to the end of the list"""
	leftPointer = 0

	for rightPointer in range(len(prime_numbers)):
		if prime_numbers[rightPointer] % 2 == 0:
			prime_numbers[leftPointer], prime_numbers[rightPointer] = prime_numbers[rightPointer], prime_numbers[leftPointer]
			leftPointer += 1
	
	return (prime_numbers)
	
primes = [2, 4, 3, 5, 7, 9, 10, 11]
print(moving_odd(primes))
