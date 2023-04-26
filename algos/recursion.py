def findFactorialRecursive(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    fact = number * findFactorialRecursive(number - 1)
    return fact

def findFactorialIterative(number):
    factorial = 1
    for num in range(number,0, -1):
        factorial *= num
    return factorial

def fibRecursive(n):
    if n < 2:
        return n
    return fibRecursive(n-1) + fibRecursive(n-2)

def fibIterative(n):
    arr = [0, 1]
    if len(arr) > 2:
        for i in range (2, n+1):
            arr.append(arr[i-2] + arr[i+2])
        return arr[n]

print(fibIterative(8))