'''
************************
Auhtor: Pranav Surampudi
Date: 10 Aug 2018
Encoding: utf-8
*************************
'''
def calculate_hand_len(hand):
    """compute the alphabets in a hand"""
    temp_list = list(hand.values())
    ans = sum(temp_list)
    return ans
def main():
    """Main Function"""
    number = input()
    adict = {}
    for i in range(int(number)):
        data = input()
        i += 1#Line written for pylint compliance
        lima = data.split()
        adict[lima[0]] = int(lima[1])
    print(calculate_hand_len(adict))
if __name__ == "__main__":
    main()
