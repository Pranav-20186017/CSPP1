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
    for i in range(limit):
        temp = input().split(" ")
        dic = tokenize(temp)
    print(dic)
if __name__ == '__main__':
    main()
