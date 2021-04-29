import square   

def fourthPower(x):
    '''
    x: int or float
    '''
    return square.square(square.square(x))

print(fourthPower(-2.49))