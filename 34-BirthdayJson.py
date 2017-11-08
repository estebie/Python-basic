"""
Exercise 34: Birthday JSON

In the previous exercise we created a dictionary of famous scientists’ birthdays. 

In this exercise, modify your program from Part 1 to load the birthday dictionary 
	from a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
	and update the JSON file you have on disk with the scientist’s name. 

If you run the program multiple times and keep adding new names, 
	your JSON file should keep getting bigger and bigger.
"""

import json, os
from datetime import datetime

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def loadBirthdays():
	with open('Birthdays.json', 'r') as f:
		return json.load(f)

def list(birthdays):
	cls()
	print("Welcome to the birthday dictionary. We know the birthdays of:\n")
	for key, value in birthdays.items():
		print(key)

def viewEntry(birthdays):
	cls()
	try:
		key = input("Who's birthday do you want to look up? ")
		print(birthdays[key])
	except KeyError:
		print("Scientist not found!")

def addEntry(birthdays):
	cls()
	name = input("Input scientist name: ")
	date = input("Input date in mm/dd/yy: ")

	with open("Birthdays.json", "w") as file:
		birthdays[name] = date
		json.dump(birthdays, file)

	print("Birtday Added Successfully")


if __name__ == '__main__':
	birthdays = loadBirthdays()

	while(True):
		while(True):
			cls()
			try:
				choice = int(input("""Please select an operation:
					\n[1]View Birtday Lists \n[2]View Birthday \n[3]Add Entry \n[4]Exit \n\nChoice: """))
				if (choice > 0 and choice < 5):
					break
				else:
					input("\nInput Error!!!! Press any key to continue...\n")
					cls()
			except ValueError:
					input("\nInput Error!!!! Press any key to continue...\n")
					cls()

		if choice == 1:
			list(birthdays)
		elif choice == 2:
			viewEntry(birthdays)
		elif choice == 3:
			addEntry(birthdays)
		else:
			break
		input("\nPress any key to continue...")
	input()