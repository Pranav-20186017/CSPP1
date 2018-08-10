'''
***************************
Author: Pranav Surampudi
Date: 10 Aug 2018
Encoding: Utf-8
**************************
'''
def updateHand(hand, word):
    """Returns an updated hand """
    for i in word:
        if i in list(hand.keys()):
            hand[i] -= 1
    return hand    
def main():
    """Main Function"""
    n = input()
    adict = {}
    for i in range(int(n)):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    data1 = input()
    print(updateHand(adict, data1))
if __name__ == "__main__":
    main()