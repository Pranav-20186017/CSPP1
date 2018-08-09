
'''
************************************
Author : Pranav Surampudi 
Date : 09  August 2018
Encoding: utf-8
***********************************
'''

def biggest(val):
    '''
    This returns the biggest element in a list
    '''
    sum_t = 0
    if isinstance(val, (tuple, list)):
        for loop in val:
            if isinstance(lo_op, (tuple, list)):
                sum_t += biggest(lo_op)
            else:
                sum_t += 1
    else:
        sum_t += 1
    return sum_t

def main():
    """Main Function"""
    adict = {(1, 2):[1], 4:[[9, 0], 9], 3:[9, 8], 'pranav':'pranavsharma67S#'}
    cou = 0
    for loop in a_dict:
        return_val = biggest(adict[loop])
        if cou < return_val:
            cou = return_val
            string = loop
    print(string)


if __name__ == "__main__":
    main()
