'''
    Author: Pranav Surampudi
    date : 16-08-2018
'''
def hand_values(hand):
    return sorted(set(["--23456789TJQKA".index(c) for c,x in hand]),reverse=True)
def is_straight(ranks):
    return (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5) or (ranks[1:5] == [5,4,3,2] and ranks[0] == 14 ) 
def is_flush(hand):
    value_set = []
    for i in hand:
        value_set.append(i[1])
    return len(value_set) == 1
def kind(ranks, n):
    for i in ranks:
        if ranks.count(i) == n:
            return i
def is_two_pair(ranks):
    high_rep = kind(ranks,2)
    low_rep = kind(sorted(ranks), 2)
    if high_rep != low_rep:
        return high_rep, low_rep, ranks
def hand_rank(hand):
    rank = hand_values(hand)
    if is_straight(rank) and is_flush(hand)
        return 8, rank
    if kind(rank, 4):
        return 7, kind(rank, 4), rank
    if kind(rank,3) and kind(rank, 2):
        return 6, kind(rank, 3), kind(rank,2), rank
    if is_flush(hand):
        return 5, rank
    if is_straight(rank):
        return 4, rank
    if kind(rank, 3):
        return 3, kind(rank, 3), rank
    if is_two_pair(hand):
        return 2, is_two_pair(rank)
    if kind(rank, 2):
        return 1, kind(rank), rank
    return 0, rank
def poker(hands):
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
