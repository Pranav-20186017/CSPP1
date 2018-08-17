'''
    Document Distance - A detailed description is given in the PDF
'''
def generate_list(input1):
    '''generate a dictionary of words'''
    new_input_1 = str(input1.lower())
    spec_char = "!@#$%^&*(),-_+=;:.?\n"
    ver_2_inp1 = ""
    for i in new_input_1:
        if i not in spec_char:
            ver_2_inp1 += i
    temp1 = ver_2_inp1.split()
    return temp1
def remove_stopwords(l1, l2):
    stopwords = load_stopwords("stopwords.txt")
    #print(stopwords)
    removal= list(stopwords.keys())
    #print(removal)
    for i in l1:
    	if i in removal:
    		l1.remove(i)
    print(l1)
# def similarity(dict1, dict2):
#     '''
#         Compute the document distance as given in the PDF
#     '''
#      pass
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

    l1 = generate_list(input1)
    l2= generate_list(input2)
    #generate_dic(l1, l2)
    # print(l1)
    # print(l2)
    remove_stopwords(l1, l2)
if __name__ == '__main__':
    main()
