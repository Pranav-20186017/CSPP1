'''
*********************************
Author: Pranav Surampudi
Date: 1 October 2018
Encoding: utf-8
**********************************
'''
def selection_sort(array):
    b = []
    st = "["
    length = len(array)
    for i in range(0, length):
        temp = min(array)
        ind = array.index(temp)
        b.append(temp)
        del array[ind]
    for i in range(0,len(b)):
        st = st + b[i] + ", "
    res = st[:-2] + "]"
    return res
def main():
    n = int(input())
    for i in range(n):
        a = input().split(" ")
        result = selection_sort(a)
        print(result)
if __name__ == "__main__":
    main()