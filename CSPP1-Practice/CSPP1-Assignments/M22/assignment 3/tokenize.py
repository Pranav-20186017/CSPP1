'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(temp):
    '''generate tokens'''
    new_list = []
    length = len(temp)
    for i in range(length):
        string = str(temp[i])
        string = string.strip('",.;')
        new_list.append(string)
    dictionary = dict()
    for i in new_list:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary
def main():
    '''main function'''
    limit = int(input())
    i = 0
    new_val = []
    while i < (limit):
        list_val = input().split(" ")
        new_val += list_val
        dic = tokenize(new_val)
        i += 1
    print(dic)
if __name__ == '__main__':
    main()
