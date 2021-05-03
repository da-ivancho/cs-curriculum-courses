def gcdIter(a, b):
    '''
    a: int > 0
    b: int > 0
    returns int (greatest commong divisor)
    '''
    gcdTemp = min(a, b)
    gcd = gcdTemp
    while gcdTemp >= 1:
        if a % gcdTemp == 0 and b % gcdTemp == 0:
            gcd = gcdTemp
            break
        gcdTemp -= 1
    
    return gcd

# Test cases
print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(7,12))
print(gcdIter(96,256))
print(gcdIter(112,98))