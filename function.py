def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result=[]
    while a < n:
        result=result+[a]
        a, b = b, a+b
    return result

fib(2000)

print type(fib) 

print fib(100)

