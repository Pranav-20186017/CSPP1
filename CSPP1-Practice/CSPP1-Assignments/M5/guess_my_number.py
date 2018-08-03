'''
Author: Pranav Surampudi
Date: 3 August 2018
Encoding: UTF-8
'''
MAX = 100
MIN = 0
CH = ''
while CH != 'c':
    GUESS = (MIN + MAX)// 2
    print("is your guess "+ str(GUESS))
    CH = input("Enter your choice: ")
    if CH == 'l':
        MIN = GUESS
    else:
        MAX = GUESS
print("The number you guessed is "+ str(GUESS))
