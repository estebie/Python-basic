import random

playFlag = True
numGuess, numGuesses, numRandom = 0, 1, random.randint(0,9)

while playFlag:
		guess = int(input("Please input your guess number: "))

		if guess < numGuess:
			print("Guess is to low")
		elif guess > numGuess:
			print("Guess is to high")
		else:
			print("Exact guess! with ", numGuesses, " guesses")
			break

		numGuesses += 1
		play = input("Do you want to continue? If not input 'exit' ")

		if play == 'exit':
				break

input()