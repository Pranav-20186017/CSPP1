'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
****************
Author: Pranav Surampudi
Date: 04 August 2018
Encoding: utf-8
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    flag = 0
    num = int_input
    product = 1
    if num == 0:
        print(num)
        exit()
    if num < 0:
        flag = flag +1
        num = num * -1
    while num != 0:
        temp = num % 10
        product = product * temp
        num = num // 10
    if flag == 0:
        print(product)
    else:
        print(product * -1)
if __name__ == "__main__":
    main()
