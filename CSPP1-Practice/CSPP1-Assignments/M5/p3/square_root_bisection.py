'''
Author: Pranav Surampudi
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """ This function computes
    the square root of a given number"""
    num = input()
    epsilon = 0.01
    low = 0
    high = int(num)
    ans = (high + low) / 2.0
    while abs(ans ** 2 - int(num)) >= epsilon:
        if ans ** 2 < int(num):
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    print(ans)
if __name__ == "__main__":
    main()
