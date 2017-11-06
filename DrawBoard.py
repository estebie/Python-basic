"""
Exercise 24: Draw A Game Board
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by
"""

import os

def draw_horizontal(xDimension):
	print(" _____ " * xDimension)

def draw_vertical(xDimension, values):
	for x in range(3):
		if (x == 1):
			print("|  %s   |  %s   |  %s   |" % (values[0],values[1],values[2]))
		else:
			print("|      " * (xDimension + 1))

def draw_board(xDimension, yDimension, board):
	cls()
	for x in range(yDimension):
		draw_horizontal(xDimension)
		draw_vertical(xDimension, board[x])
	draw_horizontal(xDimension)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
	xDimension = int(input("Please input x dimension: "))
	yDimension = int(input("Please input y dimension: "))
	board = [['-','-','-'], ['-','-','-'],['-','-','-']]
	draw_board(xDimension,yDimension, board)
	input()


