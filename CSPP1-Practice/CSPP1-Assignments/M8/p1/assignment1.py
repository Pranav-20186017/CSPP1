"""
*********************************
Author: Pranav Surampudi
Date: 7 August 2018
"""
import sys
sys.setrecursionlimit(2500000)
def factorial(number):
    """Conpute Factorial"""
    if number <= 1:
        return 1
    return number * factorial(number - 1)
def main():
    """Main Function"""
    a_var = input()
    print(factorial(int(a_var)))
if __name__ == "__main__":
    main()
