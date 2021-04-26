'''
Assume that two variables, varA and varB, are assigned values, either numbers or strings.
Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

"string involved" if either varA or varB are strings
"bigger" if varA is larger than varB
"equal" if varA is equal to varB
"smaller" if varA is smaller than varB
'''
# Test 1
varA = 8
varB = "adios"
# Test 2
varA = -8
varB = -10
# Test 3
varA = "bonjour"
varB = "bonjour"
# Test 4
varA = -1
varB = -1
# Test 5
varA = -8
varB = -3

if type(varA) == str or type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")
