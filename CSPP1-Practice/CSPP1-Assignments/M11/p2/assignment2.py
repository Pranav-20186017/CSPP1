'''
***************************
Author: Pranav Surampudi
Date: 10 Aug 2018
Encoding: Utf-8
**************************
'''
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
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