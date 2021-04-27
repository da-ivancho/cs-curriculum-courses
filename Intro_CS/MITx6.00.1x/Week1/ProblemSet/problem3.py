'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
'''
s = 'azcbobobegghakl'
longest = ''
temp = s[0]
for idx in range(len(s)-1):
    if s[idx+1] >= s[idx]:
        temp += s[idx+1]
        print(temp)
        if len(temp) > len(longest):
            longest = temp
    else:
        if len(temp) > len(longest):
            longest = temp
            temp = s[idx+1]
        else:
            temp = s[idx+1]

print('Longest substring in alphabetical order is:', longest)