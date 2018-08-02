#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

'''
Author: Panav Surampudi
Date: 2 August 2018
Encoding: UTF-8
'''
def main():
    """this function prints the number of vowles in the input string"""
    s = input()
    v = ['a','e','i','o','u']
    vc = 0
    for i in s:
        if i in v:
            vc += 1
    print(vc)

if __name__== "__main__":
    main()
