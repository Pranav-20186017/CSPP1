'''
Author: Pranav Surampudi
Date: 2 August 2018
Encding: UTF-8
'''
def main():
    """This fucntion computes the longest substring,
    that is in alphabetical order in a given string"""
    s_t = input()
    m_l = 0
    curre_point = s_t[0]
    next_point = s_t[0]
    for i in range(0, len(s_t)-1):
        if s_t[i+1] >= s_t[i]:
            curre_point += s_t[i]
            if len(curre_point) > m_l:
                m_l = len(curre_point)
                next_point = curre_point
        else:
            curre_point = s_t[i+1]
        i = i + 1
    print(next_point)
if __name__ == "__main__":
    main()
