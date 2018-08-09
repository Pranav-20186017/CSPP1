'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

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
def get_guessed_word(secret_word, letters_guessed):
    """Hangman Method"""
    temp_list = list(secret_word)
    ans = ""
    for i in temp_list:
        if i in letters_guessed:
            ans += i
        else:
            ans += '_'
    return ans
def get_available_letters(letters_guessed):
    """Return the values that are not in the guessed letters,
    but are a part of the alphabetical order"""
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ans_string = ""
    for i in alpha:
        if i not in list(letters_guessed):
            ans_string += i
    return ans_string
def is_already_guessed(s, letters_guessed):
    if s in letters_guessed:
        print("OOPS You have already selected that letter")
def hangman(secretWord):
    print("I am thinking of a word that is "+ str(sec_len)+ " long")
    guess = 8
    u = '_'
    flag = 0
    letters_guessed=[]
    while(guess>=1):
        print("Guesses Left: ",guess)
        s= input("enter a letter: ")
        letters_guessed.append(s)
        if s in secretWord and sec_len>0:
            t= (get_guessed_word(secretWord, letters_guessed))
            print(t)
            print(get_available_letters(letters_guessed))
            flag += 1
            sec_len -= 1
            if t==secretWord:
                print("The word is :" + str(secretWord))
                print("You have won")
                break
            if flag > 2:
                is_already_guessed(s, letters_guessed)
        elif s not in secretWord:
            print("OOPS That was a Wrong Guess")
            print(get_available_letters(letters_guessed))
            print(get_guessed_word(secretWord, letters_guessed))
            guess -= 1
            if guess < 1:
                print("YOU HAVE LOST")
                exit()
        else:
           break


def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
