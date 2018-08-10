'''
***************************
Author: Pranav Surampudi
Date: 10 Aug 2018
Encoding: Utf-8
**************************
'''
def update_hand(hand, word):
    """Returns an updated hand """
    for i in word:
        if i in list(hand.keys()):
            hand[i] -= 1
    return hand
def main():
    """Main Function"""
    number = input()
    adict = {}
    for i in range(int(number)):
        data = input()
        lima = data.split()
        adict[l[0]] = int(lima[1])
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
