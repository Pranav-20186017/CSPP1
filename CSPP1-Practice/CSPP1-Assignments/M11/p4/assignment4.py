'''
************************
Auhtor: Pranav Surampudi
Date: 10 Aug 2018
Encoding: utf-8
*************************
'''
def calculateHandlen(hand):
    """compute the alphabets in a hand"""
    temp_list = list(hand.values())
    ans = sum(temp_list)
    return ans
def main():
    """Main Function"""
    n = input()
    adict = {}
    for i in range(int(n)):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    print(calculateHandlen(adict))
if __name__ == "__main__":
    main()
