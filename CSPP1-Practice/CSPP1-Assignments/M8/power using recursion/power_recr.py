"""
*************************
Auhtor: Pranav Surampudi
Date: 7 August 2018
Encoding: Utf-8
************************
"""
def recur_power(base, exp):
    """Compute expoent using recursion"""
    if exp == 0:
    	return 1
    if exp == 1:
        return base * 1
    if exp != 1:
        return base * recur_power(base, exp-1)
def main():
    """Main Function"""
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
