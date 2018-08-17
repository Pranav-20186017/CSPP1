'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def tokenize(input_val):
    """Split strings into tokens"""
    word_list1 = []
    words_list = input_val.lower().split()
    for word in words_list:
        word_list1.append(re.sub('[^a-z]', "", word).strip())
    return word_list1
def build_dict(dictionary, words_list, index):
    '''build a dictionary'''
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        length = len(word)
        if word not in stopwords and length > 0:
            if word not in dictionary:
                dictionary[word] = [0, 0]
            dictionary[word][index] += 1
    return dictionary

def calculate_distance(dictionary):
    """Compute the distance"""
    num = 0
    den1 = 0
    den2 = 0
    for a, b in dictionary.values():
        num += a * b
        den1 += a ** 2
        den2 += b ** 2
    return num/(math.sqrt(den1)*math.sqrt(den2))
def similarity(d1, d2):
    '''
        Compute the document distance as given in the PDF
    '''
    common_dict = dict()
    string1_words = tokenize(d1)
    string2_words = tokenize(d2)
    common_dict = build_dict(common_dict, string1_words, 0)
    common_dict = build_dict(common_dict, string2_words, 1)
    return calculate_distance(common_dict)
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

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
