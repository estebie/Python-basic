import random

def cows(randomNumber, guessNumber):
	correct = 0

	for x in range(0,4):
		if(list(randomNumber)[x] == list(guessNumber)[x]):
			correct = correct + 1
	return correct


if __name__ == "__main__":
	guessNumber = '0'
	errorFlag, guessCount = 0, 0, 
	playFlag = True
	randomNumber = str(random.randint(1000,9999))

	print(randomNumber)
	while playFlag:
		while (len(guessNumber) < 4):
			
			if errorFlag:
				print("Error guess is less than 4 digits!")

			guessNumber = input("Please input the 4 digit guess: ")
			errorFlag = 1
			
		guessCount += 1
		correct = cows(randomNumber, guessNumber)

		if correct == 4:
			print("Exact guess! with ", guessCount, " guess/es")
			break
		else:
			print("Cows: ", correct, " Bulls: ", 4-correct)
			errorFlag = 0
			guessNumber = '0'

		play = input("Do you want to continue? If not input 'exit' ")

		if play == 'exit':
				break

	input()