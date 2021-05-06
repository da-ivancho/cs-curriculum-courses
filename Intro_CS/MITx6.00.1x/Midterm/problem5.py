def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    returns: list of keys with the value target
    '''
    keys = []
    for k, v in aDict.items():
        if v == target:
            keys.append(k)
    
    keys.sort()
    return keys

# Tests
print(keysWithValue({}, 10))
print(keysWithValue({1: 2, 2: 2, 3: 3, 7: 0, 8: 0, 10: 2}, 4))
print(keysWithValue({10: 1, 5: 0}, 3))
print(keysWithValue({0: 0, 8: 2, 2: 0, 5: 0, 9: 2}, 2))
print(keysWithValue({1: 2, 9: 2, 6: 0, 7: 2}, 2))
print(keysWithValue({0: 1, 2: 2, 3: 0, 4: 3, 5: 2, 6: 3, 8: 4, 9: 4, 10: 0}, 3))
print(keysWithValue({8: 1, 4: 1, 5: 1, 6: 2, 7: 0}, 1))
print(keysWithValue({9: 1, 2: 2, 3: 0, 4: 1, 7: 1}, 0))