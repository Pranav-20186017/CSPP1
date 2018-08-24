'''
************************************************
Author: Pranav Surampudi
Date: 24 August 2018
Encoding: utf-8
************************************************
'''
def isvalidinput(board):
    '''check for validity of input'''
    x_sum = 0
    o_sum = 0
    sum_val = 0
    for i in board:
        x_sum += i.count('x')
        o_sum += i.count('o')
        sum_val += i.count('o') + i.count('x') + i.count(".")
    if sum_val != 9:
        print("invalid input")
        return None
    if x_sum - o_sum not in (0, 1, -1):
        print("invalid game")
        return None
    return True
def checkgame(board):
    '''evaluate the game'''
    count = 0
    length = len(board)
    for i in range(length):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            count += 1
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            count += 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        count += 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        count += 1
    if count > 1:
        print("invalid game")
    else:
        return True
    return None
def checkhorizantal(board):
    '''check horizontal rows'''
    length = len(board)
    for i in range(length):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    return None
def checkvertical(board):
    '''check vertical rows'''
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    return None
def checkdiagonal(board):
    '''check diagonals'''
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None
def checkwinner(board):
    '''compute the winner'''
    winner = checkhorizantal(board)
    winner1 = checkvertical(board)
    winner2 = checkdiagonal(board)
    exp_one = winner and winner1
    exp_two = winner1 and winner2
    exp_three = winner and winner2
    if (exp_one) or (exp_two) or (exp_three):
        return "invalid game"
    if winner:
        return winner
    if winner1:
        return winner1
    if winner2:
        return winner2
    return "draw"
def main():
    '''main method'''
    board = []
    i = 0
    while i < 3:
        board.append(input().split())
        i += 1
    if isvalidinput(board) and checkgame(board):
        print(checkwinner(board))
main()
