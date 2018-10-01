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
    for i in range(0, len(basic)):
        string = string + basic[i] + ", "
    result = string[:-2] + "]"
    return result
def main():
    n = int(input())
    for i in range(n):
        a = input().split(" ")
        result = selection_sort(a)
        print(result)
if __name__ == "__main__":
    main()
