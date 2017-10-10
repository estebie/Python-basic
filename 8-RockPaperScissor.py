choice = ['p', 'r', 's']
p1, p2 = 'x', 'x'
win = {'p':'r', 'r':'s', 's':'p'}
errMsgFlag, playFlag = False, True


while playFlag:
	while ((p1 not in choice) | (p2 not in choice)):
		if errMsgFlag:
			print("Input error please input characters again!")
		
		p1 = input("Player 1 please take your pick ['r' 'p' 's']: ")
		p2 = input("Player 2 please take your pick ['r' 'p' 's']: ")
		
		errMsgFlag = True

	if p1 == p2:
		print("Match is a draw!")
	elif(win[p1] == p2):
		print("Player 1 wins!")
	else:
		print("Player 2 wins!")

	play = input("Do you wanna play again? If yes please input 'y': ")

	if play != 'y':
		break
	
	p1, p2, errMsgFlag  = 'x', 'x', False
