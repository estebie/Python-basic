'''
Exercise 35: Birthday Months

In the previous exercise we saved information about famous scientists’ names 
	and birthdays to disk. In this exercise, load that JSON file from disk, 
	extract the months of all the birthdays, and count how many scientists 
	have a birthday in each month.

Your program should output something like:

{
	'May': 3,
	'November': 2,
	'December': 1
}
'''
import json
from collections import Counter

def loadBirthdays():
	with open('BirthdayMonths.json', 'r') as f:
		return json.load(f)

def birthdayMonthsJson(birthdays):
	num_to_string = {
		1: 'January',
		2: 'February',
		3: 'March', 
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'August',
		9: 'September',
		10: 'October',
		11: 'November',
		12: 'December'
	}

	months = []

	for key, birthday_string in birthdays.items():
		month = int(birthday_string.split('/')[0])
		months.append(num_to_string[month])
	return Counter(months)

if __name__ == '__main__':
	birthdays = loadBirthdays()
	print(birthdayMonthsJson(birthdays))
	input()

