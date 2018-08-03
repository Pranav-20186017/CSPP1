'''
Author : Pranav
Date : 03 August 2018
Encoding: UTF-8
'''
def main():
    ''' This function prints the square root
    of given number in Approximation method'''
    square = int(input())
    epsilon = 0.01
    guess = 0.0
    step = 0.1
    while abs(guess**2 - square) >= epsilon:
        if guess <= square:
            guess += step
        else:
            break
    if abs(guess**2 - square) >= epsilon:
        print(" Failed to compute Square root of given number")
    else:
        print(guess)
if __name__ == "__main__":
    main()
