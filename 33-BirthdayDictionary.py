"""
Exercise 33: Birthday Dictionary

For this exercise, we will keep track of when our friend’s birthdays are, 
	and be able to find that information based on their name. 

Create a dictionary (in your file) of names and birthdays. 

When you run your program it should ask the user to enter a name, 
	and return the birthday of that person back to them. 

The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""
if __name__ == '__main__':
	birthdays = {'Albert Einstein': '04/14/1879', 
		'Ada Lovelace': '12/10/1815', 
		'Benjamin Franklin': '01/17/1706'}

	print("Welcome to the birthday dictionary. We know the birthdays of:")
	for key, value in birthdays.items():
		print(key)

	while(True):
		try:
			key = input("Who's birthday do you want to look up? ")
			print(birthdays[key])
			break
		except KeyError:
			print("Scientist not found!")
	input()
