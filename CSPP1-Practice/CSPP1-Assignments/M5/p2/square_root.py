'''
Author: Pranav Surampudi
Date: 03 August 2018
Encoding: UTF-8
'''
def main():
    """This function computes the square root
    of a given number using approximation method"""
    square = 121
    epsilon = 0.01
    guess = 0.0
    increment = 0.1
    while abs(guess**2 - square) >= epsilon:
        guess += increment
    if abs(guess**2 - square) >= epsilon:
        print('Failed to find the square root of', square)
    else:
        print(round(guess))
if __name__ == "__main__":
    main()
