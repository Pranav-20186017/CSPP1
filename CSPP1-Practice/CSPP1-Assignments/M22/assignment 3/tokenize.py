'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(temp):
	dictionary = dict()
	for i in temp:
		if i in dictionary.keys():
			dictionary[i] += 1
		else:
			dictionary[i] = 1
	return dictionary
def main():
    limit = int(input())
    for i in range(limit):
    	temp = input().split(" ")
    	dic = tokenize(temp)
    print(dic)
if __name__ == '__main__':
    main()
