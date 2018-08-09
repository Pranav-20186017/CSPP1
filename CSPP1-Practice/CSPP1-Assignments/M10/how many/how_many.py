#Exercise : how many
# write a procedure, called how_many,
#which returns the sum of the number of values associated with a dictionary.
'''''
***********************************************
Author: Pranav Surampudi
Date: 9 August 2018
Encoding: Utf-8
*************************************************
'''
def how_many(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count_values = 0
    for i in a_dict:
        count_values += len(a_dict[i])
    return count_values

def main():
    """Main Function"""
    a_dict = {}
    test_cases = int(input())
    for i in range(test_cases):
        s = input()
        i += 1
        l = s.split()
        if l[0][0] not in a_dict:
            a_dict[l[0][0]] = [l[1]]
        else:
            a_dict[l[0][0]].append(l[1])
    print(how_many(a_dict))
if __name__ == "__main__":
    main()
