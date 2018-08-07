"""
************************
Author: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
************************
"""
def iter_power(base, exp):
    """computer the exponent of a given base"""
    temp = 1
    if exp == 0:
        return 1
    i = 1
    while i <= exp:
        temp *= base
        i += 1
    return temp
def main():
    """Main Function"""
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
