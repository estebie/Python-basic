"""
Ëxercise 30: Pick Word

This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words 
	from the SOWPODS dictionary. 
"""

import re, random

def pick_word():
	with open('Sowpods.txt', 'r') as file:
		words = file.readlines()
		return words[random.randint(0, len(words) - 1)]
	return ''
		
if __name__ == "__main__":
	print(pick_word())
	input()
