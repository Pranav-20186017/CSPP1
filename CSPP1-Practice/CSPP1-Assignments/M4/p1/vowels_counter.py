'''
Author: Panav Surampudi
Date: 2 August 2018
Encoding: UTF-8
'''
def main():
    """this function prints the number of \
    vowles in the input string"""
    s_t = input()
    v_d = ['a', 'e', 'i', 'o', 'u']
    v_c = 0
    for i in s_t:
        if i in v_d:
            v_c += 1
    print(v_c)

if __name__ == "__main__":
    main()
