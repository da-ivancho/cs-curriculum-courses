def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) < 1:
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        middleChar = len(aStr) // 2
        if char == aStr[middleChar]:
            return True
        else:
            if char > aStr[middleChar]:
                return isIn(char, aStr[middleChar+1:])
            else:
                return isIn(char, aStr[:middleChar])

# Test cases
print(isIn('a', ''))
print(isIn('g', 'ahkkkwwxz'))
print(isIn('u', 'aceefhikklqsuuv'))
print(isIn('q', 'cqry'))
print(isIn('p', 'degjmmmsuuvwxxy'))