def applyToEach(L, f):
    '''
    assumes L is a list, f a function
    mutates L by replacing each element,
    e, of L by f(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])

def absolute(a):
    return abs(a)

def plusOne(a):
    return a + 1

def square(a):
    return a**2

#Test
testList = [1, -4, 8, -9]
applyToEach(testList, absolute)
print(testList)
testList = [1, -4, 8, -9]
applyToEach(testList, plusOne)
print(testList)
testList = [1, -4, 8, -9]
applyToEach(testList, square)
print(testList)

