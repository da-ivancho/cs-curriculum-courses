# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
      if letter not in lettersGuessed:
        return False
    
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lettersStr = ''
    for letter in secretWord:
      if letter in lettersGuessed:
        lettersStr += letter
      else:
        lettersStr += ' _ '
    
    return lettersStr



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    lettersNotGuessed = ''

    for letter in letters:
      if letter not in lettersGuessed:
        lettersNotGuessed += letter
    
    return lettersNotGuessed
     
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    
    while guessesLeft > 0:
      print('-------------')
      print('You have ' + str(guessesLeft) + ' guesses left.')
      print('Available letters:', getAvailableLetters(lettersGuessed))
      guess = input('Please guess a letter:')
      guess = guess.lower()

      if guess in lettersGuessed:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      else:
        lettersGuessed.append(guess)
        if isWordGuessed(secretWord, lettersGuessed):
          print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
          print('-------------')
          break
        else:
          if guess in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
          else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1

    if isWordGuessed(secretWord, lettersGuessed):
      print('Congratulations, you won!')
    elif guessesLeft == 0:
      print('Sorry, you ran out of guesses. The word was:', secretWord)
  


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# Unit Tests
""" print("isWordGuessed")
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print("Unit Test #1:", isWordGuessed(secretWord, lettersGuessed))
print("Unit Test #2:", isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print("Unit Test #3:", isWordGuessed('coconut', ['v', 'b', 's', 'q', 'i', 'a', 'e', 'g', 'w', 'r']))
print("Unit Test #4:", isWordGuessed('broccoli', ['v', 't', 'a', 'q', 'o', 'w', 'f', 'z', 's', 'c']))
print("Unit Test #5:", isWordGuessed('lettuce', []))
print("Unit Test #6:", isWordGuessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))
print("")
print("getGuessedWord")
print("Unit Test #1", getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print("Unit Test #2", getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
print("Unit Test #3", getGuessedWord('banana', ['l', 'v', 'q', 'x', 'o', 'n', 'd', 'h', 'w', 'm']))
print("Unit Test #4", getGuessedWord('mangosteen', ['d', 'c', 'f', 'i', 'z', 'o', 'p', 'u', 's', 'r']))
print("Unit Test #5", getGuessedWord('mangosteen', []))
print("Unit Test #6", getGuessedWord('coconut', ['y', 'e', 'l', 'b', 'q', 'f', 's', 't', 'n', 'o']))
print('')
print('getAvailableLetters')
print("Unit Test #1", getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
print("Unit Test #2", getAvailableLetters([]))
print("Unit Test #3", getAvailableLetters(['s', 'm', 'u', 'k', 'x', 'd', 't', 'o', 'p', 'i', 'v']))
print("Unit Test #4", getAvailableLetters(['o', 'j', 'w']))
print("Unit Test #5", getAvailableLetters(['c', 'v', 'g', 'i', 'e']))
print("Unit Test #6", getAvailableLetters(['v', 't', 'i', 'a', 'q', 'k', 'o', 'x', 'c', 'n', 'm', 'j'])) """
