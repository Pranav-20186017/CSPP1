'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def make_dict(hand):
	dic ={}
	for i in hand:
		if i[0] in dic:
			dic[i[0]] += 1
		else:
			dic[i[0]] = 1
	return dic
def is_five_kind(hand):
	my_dic = make_dict(hand)
	if 4 in list(my_dic.values()) and 'J' in my_dic:
		return True
	return False 
def is_four_kind(hand):
	my_dic = make_dict(hand)
	if 4 in list(my_dic.values()):
		return True
	return False
# def is_full(hand):
# 	print("inside full house")
# 	my_dic = make_dict(hand)
# 	k = list(my_dic.keys())
# 	if (2 in k) and (3 in k):
# 		return True
# 	return False
def is_three_kind(hand):
	my_dic = make_dict(hand)
	if 3 in list(my_dic.values()):
		return True
	return False
def is_two_pair(hand):
	count = 0
	my_dic = make_dict(hand)
	for i in my_dic.values():
		if i == 2:
			count +=1
	if count == 2:
		return True
	return False
def is_one_pair(hand):
	print("insise op")
	my_dic = make_dict(hand)
	if 2 in list(my_dic.values()):
		return True
	return False
def is_high(hand):
	count = 0
	my_dic =  make_dict(hand)
	for i in list(my_dic.keys()):
		if i == 1:
			count += 1
	if count == 5:
		return True
	return False
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    length = len(hand)
    # print("straight")
    f_sequence = 'A123456789TJQKA'
    order = {
        '2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9,
        'Q':10, 'K':11, 'A':12}
    string = ""
    for element in order:
        for part in range(length):
            if hand[part][0] == element:
                string += element
    for loop in range(11):
        if f_sequence[loop:loop + 5] == string:
            return True
    if string[0] == '2' and string[4] == 'A':
        return True
    return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    character = hand[0][1]
    length = len(hand)
    # print("flush")
    for i in range(length):
        if hand[i][1] != character:
            return False
    return True
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_flush(hand) and is_straight(hand):
    	return 8
    if is_four_kind(hand):
    	return 7
    #if is_full(hand):
    #	return 6
    if is_flush(hand):
    	return 5
    if is_straight(hand):
    	return 4
    if is_three_kind(hand):
    	return 3
    if is_two_pair(hand):
    	return 2
    if is_one_pair(hand):
    	return 1
    else:
    	return 0
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
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
