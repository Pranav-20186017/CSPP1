'''
*****************************
Auhtor: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
****************************
'''
def gcd_recur(x_var, y_var):
    """Compute GCD using recusion"""
    while y_var:
        x_var, y_var = y_var, x_var % y_var
    return x_var
def main():
    """Inside Main"""
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
