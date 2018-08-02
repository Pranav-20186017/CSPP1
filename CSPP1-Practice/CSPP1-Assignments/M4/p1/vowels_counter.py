'''
Author: Panav Surampudi
Date: 2 August 2018
Encoding: UTF-8
'''
def main():
    """this function prints the number of \
    vowles in the input string"""
    s = input()
    v = ['a', 'e', 'i', 'o', 'u']
    vc = 0
    for i in s:
        if i in v:
            vc += 1
    print(vc)

if __name__ == "__main__":
    main()
