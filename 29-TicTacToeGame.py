"""
Exercise 29 - Tic Tac Toe Game
"""


import DrawBoard, WriteBoard, CheckBoard

draw_board = DrawBoard.draw_board
write_board = WriteBoard.write_board
check_board = CheckBoard.check_board

def check_input (xCoord, yCoord):
	if ((xCoord > 0 and xCoord < 4) and (xCoord > 0 and xCoord < 4)):
		return True
	else:
		return False

if __name__ == '__main__':
	xDimension, yDimension = 3, 3
	player1, player2 = 'O', 'X'
	board = [['-','-','-'], ['-','-','-'],['-','-','-']]
	
	while (True):

		while (True):
			try:
				draw_board(xDimension,yDimension, board)
				p1XCoord = int(input("Player 1 x coordinate move: "))
				p1YCoord = int(input("Player 1 y coordinate move: "))
				
				if (check_input(p1XCoord, p1YCoord)):
					flag = write_board(player1, board, p1XCoord, p1YCoord)

					if (not flag):
						print("Error! coordinate is already taken")
						print("Press any key to continue")
						input()
					else:
						break
				else:
					print("Error! Coordinates out of bounds")
					print("Press any key to continue")
					input()

			except ValueError:
				print("Error! Please input correct coordinate values")
				print("Press any key to continue")
				input()

		if (check_board(board, player1) == True):
			draw_board(xDimension,yDimension, board)
			print("Player 1 Wins!")
			break

		while (True):
			try:
				draw_board(xDimension,yDimension, board)
				p2XCoord = int(input("Player 2 x coordinate move: "))
				p2YCoord = int(input("Player 2 y coordinate move: "))
				
				if (check_input(p2XCoord, p2YCoord)):
					flag = write_board(player2, board, p2XCoord, p2YCoord)

					if (not flag):
						print("Error! coordinate is already taken")
						print("Press any key to continue")
						input()
					else:
						break
				else:
					print("Error! Coordinates out of bounds")
					print("Press any key to continue")
					input()

			except ValueError:
				print("Error! Please input correct coordinate values")
				print("Press any key to continue")
				input()

		if (check_board(board, player2) == True):
			draw_board(xDimension,yDimension, board)
			print("Player 2 Wins!")
			break
	input()



