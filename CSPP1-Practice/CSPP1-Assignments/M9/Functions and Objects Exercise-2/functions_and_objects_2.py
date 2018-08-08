'''
*******************************
Author: Pranav Surampudi
Date: 8 August 2018
Encoding: utf-8
*******************************
'''
def apply_to_each(list_val, function):
    """Apply a fcuntion f to the list elements"""
    ans = []
    for j in list_val:
        ans.append(j + function)
    print(ans)
def main():
    """Main Function"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    inc = 1
    apply_to_each(list1, inc)
if __name__ == "__main__":
    main()
