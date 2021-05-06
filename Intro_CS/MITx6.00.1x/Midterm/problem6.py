def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    aListFlattened = []
    for element in aList:
        if not isinstance(element, list):
            aListFlattened.append(element)
        else:
            aListFlattened += flatten(element)
    
    return aListFlattened

# Test
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))