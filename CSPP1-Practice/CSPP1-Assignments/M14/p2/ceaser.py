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
    def shift(self, n):
        al = "-"+string.ascii_lowercase+string.ascii_lowercase
        cal = "-"+string.ascii_uppercase+string.ascii_uppercase
        ans = ""
        for i in range(0, len(self.plain)):
            if self.plain[i] in al:
                ans = ans + al[al.index(self.plain[i])+n]
            elif self.plain[i] in cal:
                ans = ans + cal[cal.index(self.plain[i])+n]
            else:
                ans += self.plain[i]
        print(ans)
    def build_dict(self, shift):
        al = "-"+string.ascii_lowercase+string.ascii_lowercase
        cal = "-"+string.ascii_uppercase+string.ascii_uppercase
        adict = {}
        for i in al:
            new_val = al[al.index(i) + shift]
            adict[i] = new_val
        for i in cal:
            new_val = cal[cal.index(i) + shift]
            adict[i] = new_val
        del adict['-']
        print(shift)
        print(adict)
        T = Ceaser(self.plain)
        T.shift(shift)
# K = ceaser("Hello, World!").build_dict(4)
# K = ceaser("Hello, World!").build_dict(8)
def main():
    string = input()
    shift_1 = int(input())
    shift_2 = int(input())
    K = Ceaser(str(string)).build_dict(int(shift_1))
    K = Ceaser(str(string)).build_dict(int(shift_2))
if __name__ == "__main__":
    main()
