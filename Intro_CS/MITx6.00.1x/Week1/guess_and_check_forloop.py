x = int(input('Enter an integer: '))
for guess in range(abs(x)+1):
    if guess**3 >= abs(x):
        break
if guess**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        guess = - guess
    print('Cube root of ', x, ' is ', guess)