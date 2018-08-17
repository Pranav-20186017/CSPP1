'''
    Document Distance - A detailed description is given in the PDF
'''
def generate_dic(input1, input2):
	new_input_1 = str(input1.lower())
	new_input_2 = str(input2.lower())
	spec_char  = "!?.,'"
	for i in new_input_1:
		if i in spec_char:
			new_input_1.replace(i,"")
	for i in new_input_2:
		if i in spec_char:
			new_input_2.replace(i,"")
	print(new_input_1)
	print(new_input_2)
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
