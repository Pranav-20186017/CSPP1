# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
Author : Pranav Surampudi
Date : 03 August 2018
Encoding: utf-8

'''
def main():
    ''' This function computes the square root
     of given number using Newton- Rapson method'''
    square = int(input())
    epsilon = 0.01
    guess = square / 2.0
    while abs(guess**2 - square) >= epsilon:
        guess = guess - (((guess ** 2) - square) / (2 * guess))
    print(guess)
if __name__ == "__main__":
    main()
