'''
**********************************
Author: Pranav Surampudi
Date: 22 August 2018
Encoding: utf-8
**********************************
'''
class Caesar:
    '''This a class for Caesar Cipher'''
    def __init__(self, string, ciph_val):
        if((isinstance(string) is not str) or isinstance(ciph_val) is not int):
            raise Exception('Not the right arguments')
        self.__ciph_val = ciph_val
        self.__string = string
    def solve_cipher(self):
        '''decrypt the cipher'''
        dec_str = ""
        for x in self.__string:
            if(ord(x) >= 65 and ord(x) <= 90):
                diff = ord(x) - 65
                diff = (diff - self.__ciph_val) % 26
                diff += 65
                dec_str += chr(diff)
            elif(ord(x) >= 97 and ord(x) <= 122):
                diff = ord(x) - self.__ciph_val
                diff = ord(x) - 97
                diff = (diff - self.__ciph_val) % 26
                diff += 97
                dec_str += chr(diff)
            else:
                if x == ' ':
                    dec_str += x
                    continue
                else:
                    dec_str += x
        a = ()
        b = dec_str
        c = self.__ciph_val
        new = a + (c, b)
        return new
def main():
    '''Main Function'''
    f = open("story.txt", "r")
    s = str("")
    for i in f.read():
        s += i
    obj = Caesar(s, 10)
    print(obj.solve_cipher())
if __name__ == "__main__":
    main()
