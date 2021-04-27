'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
# Test cases
s = 'azcbobobegghakl'
s = 'kefbooblbboboboboobobobobobobb'
s = 'qoyjxbobblcpvobobcbobobboobobobj'
#

word = 'bob'
count = 0

for idx in range(len(s)+1):
    if s[idx:idx+len(word)] == word:
        count += 1

print('Number of times bob occurs is:', count)


