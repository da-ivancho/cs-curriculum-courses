def oddTuples(aTuple):
    '''
    aTuple: tuple
    returns: tuple with odd elements from original aTuple
    '''
    oddTuple = ()
    for idx in range(0,len(aTuple),2):
        oddTuple += (aTuple[idx],)
    
    return oddTuple

#Test
print(oddTuples((13,)))
print(oddTuples((3, 0, 9, 17, 16)))
print(oddTuples((0, 20, 8, 9, 19, 18, 9, 18)))
print(oddTuples((5, 3, 11, 1, 6, 1, 10, 6)))