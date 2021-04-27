x = int(input('Enter an integer: '))
for guess in range(x+1):
    if guess**3 == x:
        print('Cube root of ', x, ' is ', guess)