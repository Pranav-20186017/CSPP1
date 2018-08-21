'''
*********************************************************************
Author: Pranav Surampudi
Date: 21 August 2018
Encoding: utf-8
********************************************************************
'''
import string
class Ceaser:
    '''class to compute a ceaser cipher for a given plain text'''
    def __init__(self, plain):
        self.plain = plain
    def shift(self, number):
        '''shift the alphabets of the plain text'''
        small_alpha = "-"+string.ascii_lowercase+string.ascii_lowercase
        cal = "-"+string.ascii_uppercase+string.ascii_uppercase
        ans = ""
        for i in range(0, len(self.plain)):
            if self.plain[i] in small_alpha:
                ans += small_alpha[small_alpha.index(self.plain[i]) + number]
            elif self.plain[i] in cal:
                ans = ans + cal[cal.index(self.plain[i]) + number]
            else:
                ans += self.plain[i]
        print(ans)
def main():
    '''main function'''
    inp_str = input()
    shift_val = int(input())
    ceaser_obj = Ceaser(inp_str)
    ceaser_obj.shift(shift_val)
if __name__ == "__main__":
    main()
