# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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



#final! 將91行secretWord改回原題目
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    ans1 = False
    for l in lettersGuessed:
        for s in secretWord:
            if l in secretWord:
                ans1 = True
            else:
                ans1 = False
               # return ans
    return ans1 


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans2 = ""
    for cha in secretWord:
            if cha in lettersGuessed:
                ans2 = ans2+ cha
            else:
                ans2 = ans2 + " _ "           
    return ans2
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    ans3 = string.ascii_lowercase
    for cha in lettersGuessed:
        if cha in ans3:
            ans3 = ans3.replace(cha,"") 
    return ans3

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
    # FILL IN YOUR CODE HERE...
   
    secretWord = chooseWord(wordlist).lower()    
    #secretWord = ""     
    gn = 8 # total number to guess as per the problem requested
    import string 
    begin = string.ascii_lowercase
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("You have "+ str(gn)+ " guesses left.")
    print("Available letters: "+ begin)
    lettersGuessed = []   
    Guessed = ""
    for action in range(int(gn)):
        rawinput = input("Please guess a letter: ")
        Guessed = rawinput.lower()    
        if Guessed in lettersGuessed: 
            print("Oops! You've already guessed that letter:"+ str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have " + str(gn) + " guesses left.")
            print("Available letters: " + getAvailableLetters(lettersGuessed))              
        else:
            lettersGuessed.append(Guessed)         
            if isWordGuessed(secretWord, lettersGuessed) == True:                             
                gn -= 1
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))     
                print("------------")
                if secretWord == str(getGuessedWord(secretWord, lettersGuessed)):
                    print("Congratulations, you won!")
                    break
                if  gn == 0 and secretWord != getGuessedWord(secretWord, lettersGuessed):
                    print("Sorry, you ran out of guesses. The word was " + secretWord)
                    break
                else:
                    print("You have " + str(gn) + " guesses left.")
                    print("Available letters: " + getAvailableLetters(lettersGuessed))                    
            else:        
                gn -= 1
                print("Oops! That letter is not in my word: "+ str(getGuessedWord(secretWord, lettersGuessed)))
                print("------------")
                if  gn == 0 and secretWord != getGuessedWord(secretWord, lettersGuessed):
                    print("Sorry, you ran out of guesses. The word was " + secretWord)
                    break
                else:
                    print("You have " + str(gn) + " guesses left.")
                    print("Available letters: " + getAvailableLetters(lettersGuessed))

print(hangman("secretWord"))                


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()

