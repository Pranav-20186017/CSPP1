# Exercise: odd

# Write a Python function, odd,
#that takes in one number and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.
'''
*************************
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
*************************
'''
def odd(number):
    """Check for the parity of a given number"""
    return number % 2 != 0
def main():
    """Main Function"""
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
