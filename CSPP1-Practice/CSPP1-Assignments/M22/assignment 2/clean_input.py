'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''clean the string'''
    final_ans = ""
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            final_ans += i
        if ord(i) >= 97 and ord(i) <=122:
            final_ans += i
        if ord(i) >=48 and ord(i) <= 57:
            final_ans += i
    return final_ans
def main():
    '''main function'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
