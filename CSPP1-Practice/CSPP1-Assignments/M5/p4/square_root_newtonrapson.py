# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
Author: Pranav Surampudi
Date: 3 August 2018
Encoding: utf-8
'''
def main():
    """This function computes the square root
    of a given number using newton rapson method"""
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    inp_number = 81.0
    guess = inp_number / 2.0
    while abs(guess * guess - inp_number) >= epsilon:
        guess = guess - (((guess ** 2) - inp_number)/ (2 * guess))

    print("Square root of "+ str(round(inp_number)) + ' is about '+ str(guess))
if __name__ == "__main__":
    main()
