def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    print("inside read matrix")

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    dimension_mat_one = input().split(',')
    actual_dimension_one = []
    for i in dimension_mat_one:
        actual_dimension_one.append(int(i))
    print(actual_dimension_one)
    matrix_one = []
    dimension_one = actual_dimension_one[0]
    for i in range(0,dimension_one):
        mat_one = (input().split(" "))
        matrix_one.append(mat_one) 
    dimension_mat_two = input().split(",")
    actual_dimension_two = []
    for i in dimension_mat_two:
        actual_dimension_two.append(int(i))
    print(actual_dimension_two)
    if actual_dimension_one[1] == actual_dimension_two[0]:
        read_matrix()
    else:
        print("Error: Matrix shapes invalid for mult")
        print("None")
        exit()


if __name__ == '__main__':
    main()
