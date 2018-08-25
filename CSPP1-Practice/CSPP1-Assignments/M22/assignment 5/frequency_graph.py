'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    new_dict = dict()
    keys = sorted(list(dictionary.keys()))
    for i in keys:
        new_dict[i] = dictionary[i]
    keys_new = list(new_dict.keys())
    vals_new = list(new_dict.values())
    hash_new = []
    for i in vals_new:
        temp = ""
        for j in range(i):
            temp += "#"
        hash_new.append(temp) 
    length = len(keys_new)
    for i in range(length):
        print(str(keys_new[i]) + " " + "-" + " " + str(hash_new[i]))
def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
