def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    count = 0
    biggest = None
    for k,v in aDict.items():
        if len(v) > count:
            biggest = k
            count = len(v)
    
    return biggest


#Test
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
