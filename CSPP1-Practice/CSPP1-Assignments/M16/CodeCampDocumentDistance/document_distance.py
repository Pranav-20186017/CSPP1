'''
    Document Distance - A detailed description is given in the PDF
'''
def generate_dic(input1, input2):
	new_inp1 = input1.lower()
	new_inp2 = input2.lower()
	return input1, input2

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
