'''
This code squares the value of x by repetitive addition.
'''
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft -= 1
print(str(x) + '*' + str(x) + " = " + str(ans))