'''
Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result:

21
'''
end = 6
result = 0

while end > 0:
    result += end
    end -= 1

print(result)

