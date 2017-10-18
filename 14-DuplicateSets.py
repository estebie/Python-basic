"""
Exercise 14: Duplicate Sets

Write a program (function!) that takes a list and returns 
	a new list that contains all the elements of the first 
	list minus all the duplicates.

Extras:

Write two different functions to do this 
	- one using a loop and constructing a list, and another using sets.

Go back and do Exercise 5 using sets, 
	and write the solution for that in a different function.
"""
def remove_duplicate(numberList):
	return list(set(numberList))


numberList = [1,2,3,4,5,5,1,2,3,5,6,8,90,199,3,4,5]
print(*remove_duplicate(numberList))
input()