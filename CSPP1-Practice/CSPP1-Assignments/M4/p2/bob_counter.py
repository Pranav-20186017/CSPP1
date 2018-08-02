'''
Author: Pranav Surampudi
Date: 2 August 2018
Encoding: UTF-8
'''
def main():
	"""This function prints the number of \
	times the string bob appears in a given input string"""
	s_t = input()
	b_c = 0
	for i in range(0, len(st)):
		if s_t[i] == 'b' and s_t[i+1] == 'o' and s_t[i+2] == 'b':
			b_c += 1
	print(b_c)

if __name__== "__main__":
	main()
