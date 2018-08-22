'''
Author : the_code_hawk
*Python script for solving Caesar's Cipher using Object Oriented Programming*
'''
#Class declaration
class caesar_cipher(object):
	"This a class for Caesar Cipher"
	def __init__(self, string,ciph_val):
		if((type(string) is not str) or type(ciph_val) is not int):
			raise Exception('Not the right arguments')
		self.__ciph_val = ciph_val
		self.__string = string
		self.__enc_dic = {}
		self.__dec_dic = {}
	#Method to decrypt the cipher
	def solve_cipher(self):
		dec_str = ""
		for x in self.__string:
			if(ord(x) >= 65 and ord(x) <= 90):
				diff = ord(x) - self.__ciph_val
				if(diff < 65):
					t = ord(x) - 65
					e = self.__ciph_val - t
					if(e >= 26):
						e -= (e % 26)
					e = 90-(e-1)
					diff = e
				dec_str += chr(diff)
				self.__dec_dic[x] = chr(diff)
			elif(ord(x) >= 97 and ord(x) <= 122):
				diff = ord(x) - self.__ciph_val
				if(diff < 97):
					t = ord(x) - 97
					e = self.__ciph_val - t
					if(e >= 26):
						e -= (e % 26)
					e = 122-(e-1)
					diff = e
				dec_str += chr(diff)
				self.__dec_dic[x] = chr(diff)
			else:
				if(x == ' '):
					dec_str += x
					continue
				else:
					dec_str += x
					self.__dec_dic[x] = x

		return dec_str
	#Method to encrypt plain text
	def encrypt_text(self):
		enc_str = ""
		for x in self.__string:
			if(ord(x) >= 65 and ord(x) <= 90):
				add = ord(x) + self.__ciph_val
				if(add > 90):
					add -= (int(add % 26) + (self.__ciph_val + 1))
				enc_str += chr(add)
				self.__enc_dic[x] = chr(add)
			elif(ord(x) >= 97 and ord(x) <= 122):
				add = ord(x) + self.__ciph_val
				if(add > 122):
					add -= (int(add % 26) + (self.__ciph_val + 1))
				enc_str += chr(add)
				self.__enc_dic[x] = chr(add)
			else:
				if(x == ' '):
					enc_str += x
					continue
				else:
					enc_str += x
					self.__enc_dic[x] = x

		return enc_str
	def encrypt_way(self):
		return self.__enc_dic
	def decrypt_way(self):
		return self.__dec_dic

#Driver Code
x = caesar_cipher("!@#$%^&*",4)
print(x.encrypt_text())
print(x.encrypt_way())

y = caesar_cipher("!@#$%^&*",4)
print(y.solve_cipher())
print(y.decrypt_way())

		