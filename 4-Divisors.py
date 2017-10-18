"""
Exercise 4: Divisors
	
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out 
	that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""
integer = int(input("Please input a number to be divided: "))

print(list(filter(lambda number: (integer % number) == 0, range(1, integer+1))))
input()