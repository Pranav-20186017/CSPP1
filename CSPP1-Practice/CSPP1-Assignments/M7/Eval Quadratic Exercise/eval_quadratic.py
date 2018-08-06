# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
#that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
'''
def eval_quadratic(a_coeff, b_coeff, c_coeff, x_var):
    """This method evaluates a quadratic equation"""
    return int((a_coeff * (x_var ** 2)) + (b_coeff * x_var) + c_coeff)
def main():
    """Main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    for x_var in data:
        temp = str(x_var).split('.')
        if temp[1] == '0':
            x_var = int(float(str(x_var)))
        else:
            x_var = x_var
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
