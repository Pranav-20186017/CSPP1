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
				diff = ord(x) - 65
				diff = (diff - self.__ciph_val) % 26
				diff += 65
				dec_str += chr(diff)
				self.__dec_dic[x] = chr(diff)
			elif(ord(x) >= 97 and ord(x) <= 122):
				diff = ord(x) - self.__ciph_val
				diff = ord(x) - 97
				diff = (diff - self.__ciph_val) % 26
				diff += 97
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
				add = ord(x) - 65
				add = (add + self.__ciph_val) % 26
				add += 65
				enc_str += chr(add)
				self.__enc_dic[x] = chr(add)
			elif(ord(x) >= 97 and ord(x) <= 122):
				add = ord(x) - 97
				add = (add + self.__ciph_val) % 26
				add += 97
				enc_str += chr(add)
				self.__enc_dic[x] = chr(add)
			else:
				if(x == ' '):
					enc_str += x
					continue
				else:
					enc_str += x
					self.__enc_dic[x] = x

		ans = tuple()
		ans += (enc_str)
		return ans
	def encrypt_way(self):
		return self.__enc_dic
	def decrypt_way(self):
		return self.__dec_dic

#Driver Code
x = caesar_cipher("p@$$w0rd",7)
print(x.encrypt_text())
#print(x.encrypt_way())

y = caesar_cipher("Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. Ro rkc loox boqscdobon pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. Sd rkc loox dro dbknsdsyx yp dro bocsnoxdc yp Okcd Mkwzec dy lomywo Tkmu Pvyboi pyb k pog xsqrdc okmr iokb dy onemkdo sxmywsxq cdenoxdc sx dro gkic, wokxc, kxn odrsmc yp rkmusxq.",10)
print(y.solve_cipher())
#print(y.decrypt_way())

		