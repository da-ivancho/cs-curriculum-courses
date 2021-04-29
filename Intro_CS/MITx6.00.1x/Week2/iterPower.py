def iterPower(base, exp):
    '''
    base: float or int
    exp: int >= 0
    return int or float
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    
    return result

print(iterPower(-3.77, 0))
print(iterPower(-4.97, 6))
print(iterPower(9.78, 7))
print(iterPower(2, 0))