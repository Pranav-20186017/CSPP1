'''
Author: Panav Surampudi
Date: 2 August 2018
Encoding: UTF-8
'''
def main():
    """this function prints the number of \
    vowles in the input string"""
    S = input()
    V = ['a', 'e', 'i', 'o', 'u']
    VC = 0
    for i in S:
        if i in V:
            VC += 1
    print(VC)

if __name__ == "__main__":
    main()
