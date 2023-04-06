def memoised_fib():
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
    return fib

def unmemoised_fib(n):
    if n < 2:
        return n
    return unmemoised_fib(n-1) + unmemoised_fib(n-2)
    

fastFib = memoised_fib()
print(fastFib(15))
print(unmemoised_fib(15))