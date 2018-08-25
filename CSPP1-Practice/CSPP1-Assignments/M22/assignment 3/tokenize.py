'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(temp,i):
    if i == 0:
        new_list=[]
        for i in range(len(temp)):
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
    limit = int(input())
    for i in range(limit):
        temp = input().split(" ")
        dic = tokenize(temp,i)
    print(dic)
if __name__ == '__main__':
    main()
