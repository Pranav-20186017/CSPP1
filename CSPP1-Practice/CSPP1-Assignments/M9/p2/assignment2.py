'''
************************************
Author: Pranav Surampudi
Date: 8 August 2018
Encoding: Utf-8
************************************
'''
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
def main():
    '''
    Main function for current assignment
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
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
