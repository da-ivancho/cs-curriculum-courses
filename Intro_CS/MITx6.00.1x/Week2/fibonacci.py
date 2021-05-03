def fib(x):
    '''
    assumes x an int >= 0
    returns Fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# Tests
print(fib(0))
print(fib(1))
print(fib(5))
print(fib(10))