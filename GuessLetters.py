"""
Exercise 31: Guess Letters

Let’s continue building Hangman. 

In the game of Hangman, a clue word is given by the program 
	that the player has to guess, letter by letter. 

The player guesses one letter at a time until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).
"""
def reveal_letter(word, guessedWord, guessedLetter):
	if (guessedLetter not in word):
		return False
	else:
		for index, letter in enumerate(word):
			if (letter == guessedLetter):
				guessedWord[index] = letter
		return True

if __name__ == '__main__':
	guessCount = 0;
	word = 'Evaporate'
	word = list(word.upper())
	guessedWord = list('_' * len(word))
	print(*guessedWord)

	while ('_' in guessedWord):
		guessedLetter = input("Input a letter: ")
		flag = reveal_letter(word, guessedWord, guessedLetter)
		
		if (not flag):
			print("Error!")
		else:
			print(*guessedWord)

		guessCount = guessCount + 1

		if ('_' not in guessedWord):
			print("You guessed the word in ", guessCount, "tries")