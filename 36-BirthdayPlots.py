"""
Exercise 36: Birthday Plots

In this exercise, use the bokeh Python library to plot a histogram 
	of which months the scientists have birthdays in! 

Because it would take a long time for you to input the months of 
	various scientists, you can use my scientist birthday JSON file. 

Just parse out the month and draw your histogram.
"""
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

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
	return dict(Counter(months))

def monthSortData(birthday_months):
	return {
		'January' : birthday_months['January'],
		'February' : birthday_months['February'],
		'March' : birthday_months['March'],
		'April' : birthday_months['April'],
		'May' : birthday_months['May'],
		'June' : birthday_months['June'],
		'July' : birthday_months['July'],
		'August' : birthday_months['August'],
		'September' : birthday_months['September'],
		'October' : birthday_months['October'],
		'November' : birthday_months['November'],
		'December' : birthday_months['December'],
	}

if __name__ == '__main__':
	birthdays = loadBirthdays()
	birthday_months = birthdayMonthsJson(birthdays)
	sorted_birthdays = monthSortData(birthday_months)

	x = []
	y = []
	x_categories = []

	for key, value in sorted_birthdays.items():
		x_categories.append(key)
		y.append(value)
	x = x_categories
	
	output_file("36-plot.html")
	p = figure()
	p=figure(x_range=x_categories)
	p.vbar(x=x, top=y, width=0.5)
	show(p)