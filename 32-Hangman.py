"""
Exercise 32: Hangman

In this exercise, we will finish building Hangman. 

In the game of Hangman, the player only has 6 incorrect guesses 
	(head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. 

In Part 2, we wrote the logic for guessing the letter and displaying 
	that information to the user. 

In this exercise, we have to put it all together and add logic 
	for handling guesses.

Copy your code from Parts 1 and 2 into a new file 
	as a starting point. 

Now add the following features:

Only let the user guess 6 times, 
	and tell the user how many guesses they have left.

Keep track of the letters the user guessed. 

If the user guesses a letter they already guessed, 
	don’t penalize them - let them guess again.

Hangman pictures credits to: https://inventwithpython.com/chapter9.html
"""
import PickWord, GuessLetters, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


pick_word = PickWord.pick_word
reveal_letter = GuessLetters.reveal_letter

HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

def game_screen(hangmanIndex, guessedWord):
	cls()
	print(HANGMANPICS[hangmanIndex])
	print(*guessedWord)

if __name__ == '__main__':
	guessCount = 0
	hangmanIndex = 0
	winFlag = False

	word = list(pick_word().strip().upper())
	guessedWord = list('_' * len(word))
	guessedLetters = []

	while(guessCount < 6):
		game_screen(hangmanIndex, guessedWord)
		guessedLetter = input("Input a letter: ").upper()
		flag = reveal_letter(word, guessedWord, guessedLetter)

		if (not flag):
			if (guessedLetter not in guessedLetters):
				guessedLetters.append(guessedLetter)
				hangmanIndex = hangmanIndex + 1

		guessCount = guessCount + 1
		
		if ('_' not in guessedWord):
			game_screen(hangmanIndex, guessedWord)
			print("You guessed the word!")
			winFlag = True
			break

	if (not winFlag):
		game_screen(hangmanIndex, guessedWord)
		print("You lost!")
	input()