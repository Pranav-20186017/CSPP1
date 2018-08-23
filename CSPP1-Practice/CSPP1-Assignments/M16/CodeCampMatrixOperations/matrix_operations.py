'''
*********************************************
Author: Pranav Surampudi
Date: 23 August 2018
Encdoing: Utf-8
**********************************************

'''
def mult_matrix(x_value, y_value, actual_dimension_one, actual_dimension_two):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if actual_dimension_one[1] == actual_dimension_two[0]:
        result = [[sum(a*b for a, b in zip(x_value_row, y_value_col)) for y_value_col in zip(*y_value)] for x_value_row in x_value]
        return result
    print("Error: Matrix shapes invalid for mult")
    return None
def add_matrix(x_value, y_value, actual_dimension_one, actual_dimension_two):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    try:
        if actual_dimension_one[0] == actual_dimension_two[0] and \
        actual_dimension_one[1] == actual_dimension_two[1]:
            result = [[x_value[i][j] + y_value[i][j]  \
            for j in range(len(x_value[0]))] for i in range(len(x_value))]
            return result
    except IndexError:
        print("Error: Invalid input for the matrix")
        exit()
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    '''main method'''
    dimension_mat_one = input().split(',')
    actual_dimension_one = []
    for i in dimension_mat_one:
        actual_dimension_one.append(int(i))
    # print(actual_dimension_one)
    matrix_one = []
    dimension_one = actual_dimension_one[0]
    for i in range(0, dimension_one):
        mat_one = (input().split(" "))
        matrix_one.append(mat_one)
    # print(matrix_one)
    dimension_mat_two = input().split(",")
    actual_dimension_two = []
    for i in dimension_mat_two:
        actual_dimension_two.append(int(i))
    # print(actual_dimension_two)
    dimension_two = actual_dimension_two[0]
    matrix_two = []
    for i in range(0, dimension_two):
        mat_two = (input().split(" "))
        matrix_two.append(mat_two)
    # print(matrix_two)
    for i in matrix_one:
        length = len(i)
        for j in range(0, length):
            i[j] = int(i[j])
    for i in matrix_two:
        length = len(i)
        for j in range(0, length):
            i[j] = int(i[j])
    print(add_matrix(matrix_one, matrix_two, actual_dimension_one, actual_dimension_two))
    print(mult_matrix(matrix_one, matrix_two, actual_dimension_one, actual_dimension_two))
if __name__ == '__main__':
    main()
