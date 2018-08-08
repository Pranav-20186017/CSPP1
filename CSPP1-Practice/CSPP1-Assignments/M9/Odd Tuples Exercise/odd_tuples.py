'''
********************************
Author: Pranav Surampudi
Date: 8 August 2018
Encoding: utf-8
********************************
'''
def odd_tuples(a_tup):
    """Return odd tuple"""
    length = len(a_tup)
    ans = ()
    for i in range(0, length+1, 2):
        ans += (a_tup[i],)
    return ans
def main():
    """Main Function"""
    data = input()
    data = data.split()
    a_tup = ()
    for j in data:
        a_tup += (int(j),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
