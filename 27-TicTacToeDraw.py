"""
Exercise 27: Tic Tac Toe Draw

This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a 
	“data structure” to store information about a tic tac toe game. 
In a tic tac toe game, the “game server” needs to know where the Xs and Os 
	are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input. 
When a player (say player 1, who is X) wants to place an X on the screen, 
	they can’t just click on a terminal. 

So we are going to approximate this clicking simply by asking the user 
	for a coordinate of where they want to place their piece.
"""

def write_board(player, board, coordinates):
	coordinates = coordinates.split(',')
	x_coordinate = int(coordinates[0]) - 1
	y_coordinate = int(coordinates[1]) - 1

	if (board[x_coordinate][y_coordinate] == 0):
		board[x_coordinate][y_coordinate] = player
		return True
	else:
		return False

def print_board(board):
	print(*board[0])
	print(*board[1])
	print(*board[2])

if __name__ == "__main__":
	board = [[0,0,0], 
			 [0,0,0], 
		     [0,0,'o']]
		     
	print_board(board)
	flag = write_board('x', board, '3,3')

	if (flag):
		print_board(board)
	else:
		print('error')

input()