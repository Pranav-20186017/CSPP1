'''
************************************
Author: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
***********************************
'''
def sumofdigits(number):
    """Compute the sum of digits in a number"""
    if number == 0:
        return 0
    return number % 10 + sumofdigits(number // 10)
def main():
    """Inside Main Function"""
    a = input()
    print(sumofdigits(int(a))) 
if __name__ == "__main__":
    main()
