'''
Author: Pranav Surampudi
Date: 3 August 2018
Encoding: UTF-8
'''
def main():
    """This function prints the number
    that the user has guessed """
    max_a = 100
    min_a = 0
    c_h = ''
    while c_h != 'c':
        guess_a = (min_a + max_a)// 2
        print("is your guess "+ str(guess_a))
        c_h = input("Enter your choice: ")
        if c_h == 'l':
            min_a = guess_a
        else:
            max_a = guess_a
    print("The number you guessed is "+ str(guess_a))


if __name__ == "__main__":
    main()
