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
        self.__ciph_val = ciph_val
        self.__string = string
    def solve_cipher(self):
        '''decrypt the cipher'''
        dec_str = ""
        for xinp in self.__string:
            if(ord(xinp) >= 65 and ord(xinp) <= 90):
                diff = ord(xinp) - 65
                diff = (diff - self.__ciph_val) % 26
                diff += 65
                dec_str += chr(diff)
            elif(ord(xinp) >= 97 and ord(xinp) <= 122):
                diff = ord(xinp) - self.__ciph_val
                diff = ord(xinp) - 97
                diff = (diff - self.__ciph_val) % 26
                diff += 97
                dec_str += chr(diff)
            else:
                if xinp == ' ':
                    dec_str += xinp
                    continue
                else:
                    dec_str += xinp
        tup = ()
        dec = dec_str
        cipher_number = self.__ciph_val
        new = tup + (cipher_number, dec)
        return new
        def __len__(self):
            return "inside length method"
def main():
    '''Main Function'''
    f_open = open("story.txt", "r")
    string = str("")
    for i in f_open.read():
        string += i
    obj = Caesar(str(string), 10)
    pylint = obj.len(string)
    pylint += 1
    print(obj.solve_cipher())
if __name__ == "__main__":
    main()
