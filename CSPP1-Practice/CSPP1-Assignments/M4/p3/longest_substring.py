'''
Author: Pranav Surampudi
Date: 2 August 2018
Encding: UTF-8
'''
def main():
    """This function prints the longest substring that
     follows the alphabetical order in a given string"""
    s = input()
    maxLen=0
    current=s[0]
    longest=s[0]
    for i in range(len(s) - 1):
        if s[i + 1] >= s[i]:
            current += s[i + 1]
            if len(current) > maxLen:
                maxLen = len(current)
                longest = current
        else:
            current=s[i + 1]    
    i += 1
    print ('Longest substring in alphabetical order is: ' + longest)
if __name__ == "__main__":
    main()
