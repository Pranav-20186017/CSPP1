'''
*********************************
Author: Pranav Surampudi
Date: 1 October 2018
Encoding: utf-8
**********************************
'''
def selection_sort(array):
    '''Function for selection sort'''
    basic = []
    string = "["
    length = len(array)
    for i in range(0, length):
        i = i + 1
        temp = min(array)
        ind = array.index(temp)
        basic.append(temp)
        del array[ind]
    for i in basic:
        string = string + i + ", "
    result = string[:-2] + "]"
    return result
def main():
    '''Main function'''
    number = int(input())
    i = 0
    while i < number:
        alphabet = input().split(" ")
        result = selection_sort(alphabet)
        print(result)
        i = i + 1
if __name__ == "__main__":
    main()
