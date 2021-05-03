def gcdRecur(a, b):
    '''
    a: int > 0
    b: int > 0
    returns int (greatest commong divisor)
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# Test Cases
print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))
print(gcdRecur(198, 144))
print(gcdRecur(20, 92))