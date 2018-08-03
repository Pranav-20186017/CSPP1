'''
Author: Pranav Surampudi
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """This fucntion checks whether or not
    a given number is a perfect cube"""
    n_a = int(input())
    t_a = 0
    for i in range(1, n_a+1, 1):
        if i**3 == n_a:
            t_a += 1
            print(str(n_a) + " is a perfect cube")
            exit()
    if t_a == 0:
        print(str(n_a)+" is not a perfect cube")
if __name__ == "__main__":
    main()
