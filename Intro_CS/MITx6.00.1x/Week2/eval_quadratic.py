'''
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic 𝑎⋅𝑥2+𝑏⋅𝑥+𝑐.
'''
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c

print(evalQuadratic(8.98, -2.24, 6.95, -3.89))