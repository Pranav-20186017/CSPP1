def checkhorizantal(board):
	for i in range(len(board)):
		if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
			return board[i][0]

def checkvertical(board):
	for i in range(len(board)):
		if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
			return board[0][i]

def checkdiagonal(board):
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[0][0]
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[0][2]


def checkwinner(board):
	winner =  checkhorizantal(board)
	if winner:
		return winner
	winner = checkvertical(board)
	elif winner:
		return winner
	winner = checkdiagonal(board)
	elif winner:
		return winner
	else:
		return "draw"

def main():
	board = []
	for i in range(3):
		board.append(input().split())
	print(checkwinner(board))

main()