"""
Exercise 26: Check Tic Tac Toe

As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, 
    not worrying about how the moves were made.
"""

def check_x(board, rowNum, player):
	row = {board[rowNum][0], board[rowNum][1], board[rowNum][2]}
	if (row == {player}):
		return True
	else:
		return False

def check_y(board, colNum, player):
	col = {board[0][colNum], board[1][colNum], board[2][colNum]}
	if (col == {player}):
		return True
	else:
		return False

def check_diagonal(board, player):
	diagonal1 = {board[0][0], board[1][1], board[2][2]}
	diagonal2 = {board[0][2], board[1][1], board[2][0]}
	if (diagonal1 == {player} or diagonal2 == {player}):
		return True
	else:
		return False

def check_board(board, player):
	if (check_diagonal(board, player) == True):
		return True
	for index in range(3):
		if (check_x(board, index, player) == True):
			return True
		elif(check_y(board, index, player) == True):
			return True
	return False

if __name__ == "__main__":
	board = [[1,0,0], 
			 [1,0,1], 
			 [0,0,1]]
	print(board[0])
	print(board[1])
	print(board[2])
	if(check_board(board, 1) == True):
		print("Winner")
	else:
		print("Loser")
