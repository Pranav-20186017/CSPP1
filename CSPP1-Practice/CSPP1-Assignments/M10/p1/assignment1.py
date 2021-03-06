'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
************************************************
Author: Pranav Surampdui
Date: 9 August 2018
Encoding: utf-8
'''
def get_available_letters(letters_guessed):
    """Return the values that are not in the guessed letters,
    but are a part of the alphabetical order"""
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ans_string = ""
    for i in alpha:
        if i not in list(letters_guessed):
            ans_string += i
    return ans_string
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
