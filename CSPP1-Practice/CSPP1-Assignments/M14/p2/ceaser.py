"""
********************************************************
Author: Pranav Surampudi
Date : 21 Aug 2018
Encoding: utf-8
*******************************************************
"""
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
                ans = ans + small_alpha[small_alpha.index(self.plain[i]) + number]
            elif self.plain[i] in cal:
                ans = ans + cal[cal.index(self.plain[i]) + number]
            else:
                ans += self.plain[i]
        print(ans)
    def build_dict(self, shift):
        '''build a dictionary of substitution values'''
        small_alpha = "-"+string.ascii_lowercase+string.ascii_lowercase
        cap_alpha = "-"+string.ascii_uppercase+string.ascii_uppercase
        adict = {}
        for i in small_alpha:
            new_val = small_alpha[small_alpha.index(i) + shift]
            adict[i] = new_val
        for i in cap_alpha:
            new_val = cap_alpha[cap_alpha.index(i) + shift]
            adict[i] = new_val
        del adict['-']
        print(shift)
        print(adict)
        temp_obj = Ceaser(self.plain)
        temp_obj.shift(shift)
# K = ceaser("Hello, World!").build_dict(4)
# K = ceaser("Hello, World!").build_dict(8)
def main():
    '''main function'''
    string = input()
    shift_1 = int(input())
    shift_2 = int(input())
    K = Ceaser(str(string)).build_dict(int(shift_1))
    K = Ceaser(str(string)).build_dict(int(shift_2))
if __name__ == "__main__":
    main()
