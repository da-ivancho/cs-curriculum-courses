def recurPower(base, exp):
    '''
    base: int or float
    exp: int >= 0
    return: int or float
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp -1)

print(recurPower(3.11, 0))
print(recurPower(-5.11, 8))
print(recurPower(2.78, 5))