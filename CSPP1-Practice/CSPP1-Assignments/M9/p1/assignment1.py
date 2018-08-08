'''
*********************************
Author: Pranav Surampudi
Date: 8 August 2018
Encoding: utf-8
**********************************
'''
def is_word_guessed(secret_word, letters_guessed):
    """Hangman Function"""
    temp_list = list(secret_word)
    count = 0
    for i in temp_list:
        if i in letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    return False
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
