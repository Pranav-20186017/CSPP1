'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import string
def clean_string(string):
    '''clean the string'''
    final_ans = ""
    small_letters = string.ascii_lowercase
    cap_letters = string.ascii_uppercase
    digits = string.digits
    for i in string:
        if i in small_letters:
            final_ans += i
        if i in cap_letters:
            final_ans += i
        if i in digits:
            final_ans += i
    return final_ans
def main():
    '''main function'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
