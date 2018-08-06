# Exercise: fourth power
# Write a Python function, fourthPower,
#that takes in one number and returns that value raised to the fourth power.
# You should use the square procedure
#that you defined in an earlier exercise exercise (you don't need to redefine square in this box;
# This function takes in one number and returns one number.
'''
************************
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
************************
'''
def square(x_var):
    """Computes square of a given number"""
    return x_var ** 2
def fourth_power(x_var):
    """Computes the fourth power of a given number"""
    temp = square(x_var)
    return temp ** 2
def main():
    """Main Function"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
