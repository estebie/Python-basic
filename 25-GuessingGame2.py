"""
Exercise 25: Guessing Game 2

In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. 
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), 
and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 
"""
def binary_slice(numberList, direction, middle):

	if (direction == '>'):
		numberList = numberList[middle+1:-1]
	elif(direction == '<'):
		numberList = numberList[0:middle-1]
	else:
		return None

	return numberList


if __name__ == "__main__":
	try:
		numberList = list(range(101))
		errMsgFlag, playFlag = False, True
		guesses = 0
		choices = ['yes', '>', '<']

		while playFlag:
			middle = len(numberList) // 2
			print("Is the number: ", numberList[middle],"?")
			choice = input("Input 'yes' if it is, if not please dictate if '>' or '<': ")

			while (choice not in choices):
				print("Error!")
				choice = input("Input 'yes' if it is, if not please dictate if '>' or '<': ")

			if choice == 'yes':
				print("Computer tried guessing your number ", guesses, " times")
				break
			
			numberList = binary_slice(numberList, choice, middle)
			guesses = guesses + 1
			
	except IndexError:
		print(":(")


