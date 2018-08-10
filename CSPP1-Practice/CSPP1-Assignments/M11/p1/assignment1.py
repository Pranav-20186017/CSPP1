'''
************************************
Author: Pranav Surampudi
Date: 10 Aug 2018
Encoding: UTF-8
************************************
'''

def get_word_score(word, number):
    """Compute the score for a given word"""
    word = word.lower()
    scrabble_letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    score = 0
    bonus = 50
    for i in word:
        score += scrabble_letter_values[i]
    score *= len(word)
    if len(word) == number:
        score += bonus
    return score
def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))
if __name__ == "__main__":
    main()
