# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.
'''
**********************************
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
**********************************
'''
def square(inp):
    """Compute the square of a number """
    return inp ** 2
# Correct
def main():
    """Main function"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
