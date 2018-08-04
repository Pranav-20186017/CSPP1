'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
*****************
Author: Pranav Surampudi
Date: 4 August 2018
Encoding: UTF-8
*****************
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    answer = ""
    sp_char = "!@#$%^&*"
    for i in str_input:
        if i in sp_char:
            answer += " "
        else:
            answer += i
    print(answer)
if __name__ == "__main__":
    main()
