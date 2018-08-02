'''
Author: Pranav Surampudi
Date: 2 August 2018
Encding: UTF-8
'''
def main():
    """This function prints the longest substring that
     follows the alphabetical order in a given string"""
    s_t = input()
    m_l = 0
    cu_st = s_t[0]
    lo_st = s_t[0]
    for i in range(len(s_t) - 1):
        if s_t[i + 1] >= s_t[i]:
            cu_st += s_t[i + 1]
            if len(cu_st) > m_l:
                m_l = len(cu_st)
                lo_st = cu_st
        else:
            cu_st = s_t[i + 1]
        i += 1
print(lo_st)
if __name__ == "__main__":
    main()
