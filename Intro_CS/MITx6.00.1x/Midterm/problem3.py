'''
Write a recursive Python function, given a non-negative integer N, 
to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0
'''
def count7(n):
    '''
    N: a non-negative integer
    '''
    if n == 0:
        return 0
    elif n%10 == 7:
        return 1 + count7(n//10)
    else:
        return count7(n//10)


#Tests
print(count7(717))
print(count7(1237123))
print(count7(8989))
print(count7(7))
print(count7(1))