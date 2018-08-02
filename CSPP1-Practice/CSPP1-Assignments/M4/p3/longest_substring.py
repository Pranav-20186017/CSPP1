'''
Author: Pranav Surampudi
Date: 2 August 2018
Encding: UTF-8
'''
def main():
    """This function prints the longest substring that
     follows the alphabetical order in a given string"""
    s_t = input()
    max_len = 0
    current = s_t[0]
    next_point = s_t[0]
    i = 0
    for i in range(len(s_t) - 1):
        if s_t[i + 1] >= s_t[i]:
            current += s_t[i + 1]
            if len(current) > max_len:
                max_len = len(current)
                next_point = current
        else:
            current = s_t[i + 1]
    i += 1
    print(next_point)
if __name__ == "__main__":
    main()
