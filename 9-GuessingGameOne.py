"""
Exercise 9: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, 
	too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

playFlag = True
numGuesses, numRandom =  1, random.randint(0,9)

while playFlag:
		guess = int(input("Please input your guess number: "))

		if guess < numRandom:
			print("Guess is to low")
		elif guess > numRandom:
			print("Guess is to high")
		else:
			print("Exact guess! with ", numGuesses, " guess/es")
			break

		numGuesses += 1
		play = input("Do you want to continue? If not input 'exit' ")

		if play == 'exit':
				break

input()