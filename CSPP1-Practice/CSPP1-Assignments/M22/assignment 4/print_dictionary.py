'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    new_dict = dict()
    keys = sorted(list(dictionary.keys()))
    for i in keys:
        new_dict[i] = dictionary[i]
    keys_new = list(new_dict.keys())
    vals_new = list(new_dict.values())
    for i in range(len(keys_new)):
        print(str(keys_new[i]) + " " + "-" + " " + str(vals_new[i]))
def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
