cube = 27
epsilon = 0.01
numGuesses = 0
low = 1
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    numGuesses += 1

print('num_guesses =', numGuesses)
print(guess, 'is close to the cube root of', cube)