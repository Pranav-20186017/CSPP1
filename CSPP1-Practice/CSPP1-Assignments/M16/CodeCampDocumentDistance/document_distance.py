'''
    Document Distance - A detailed description is given in the PDF
'''
def generate_dic(input1, input2):
	new_input_1 = str(input1.lower())
	new_input_2 = str(input2.lower())
	spec_char  = "!@#$%^&*()-_+=;:'.?"
	ver_2_inp1 = ""
	ver_2_inp2 = ""
	for i in new_input_1:
		if i not in spec_char:
			ver_2_inp1 += i
	for i in new_input_2:
		if i not in spec_char:
			ver_2_inp2 += i
	print(ver_2_inp1.replace(",",""))
	print(ver_2_inp2.replace(",",""))
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    pass

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(generate_dic(input1, input2))

if __name__ == '__main__':
    main()
