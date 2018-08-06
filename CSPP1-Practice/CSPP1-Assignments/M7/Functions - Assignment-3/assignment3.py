'''
************************
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
************************
'''
def paying_debt_off_in_a_year(balance, annual):
    """Calculate minimum payment by bisection"""
    lower = balance / 12.0
    upper = balance * (1 + annual / 12.0) ** 12 / 12
    fixed = (lower + upper) / 2.0
    while True:
        remain = balance
        for i in range(1, 13):
            remain = (remain - fixed) * (1 + annual / 12.0)
        if remain > 0:
            lower = fixed
        elif remain <= 0 and remain >= -0.001:
            break
        else:
            upper = fixed
        fixed = (lower + upper) / 2.0
    ans = "Lowest Payment: " + str(round(fixed, 2))
    print(ans)
def main():
    """Main Function """
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    paying_debt_off_in_a_year(data[0], data[1]) 
if __name__ == "__main__":
    main()
