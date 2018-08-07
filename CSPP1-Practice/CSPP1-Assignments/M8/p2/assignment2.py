'''
**************************************
Author: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
**************************************
'''
def sumofdigits(number):
    """Find Sum of digits"""
    if number == 0:
        return 0
    return number % 10 + sumofdigits(number // 10)
def main():
    """Main Function"""
    a_var = input()
    print(sumofdigits(int(a_var)))  
if __name__ == "__main__":
    main()
