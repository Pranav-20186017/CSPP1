'''
*************************************
Author: Pranav Surampdui
Date: 10 August 2018
Encoding: utf-8
*************************************
'''
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False
    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    list_t = list(hand.keys())
    flag = 0
    count = 0
    temp_list = []
    if word in word_list:
        temp_list = list(word)
        flag += 1
    for i in temp_list:
        if i in list_t:
            count += 1
        elif i not in list_t:
            return False
    if count == len(temp_list):
        flag += 1
    if flag == 2:
        return True
    else:
        return False
def main():
    word = input()
    n = int(input())
    adict = {}
    for i in range(n):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    l2 = input().split()
    print(is_valid_word(word, adict, l2))
if __name__ == "__main__":
    main()
