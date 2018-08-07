"""
*****************************
Author: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
*****************************
"""
def gcd_iter(a, b):
    """Compute GCD"""
    lim = min(a, b)
    for i in range(lim, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        i += 1
def main():
    """Main Function"""
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
