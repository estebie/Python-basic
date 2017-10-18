"""
Exercise 12: List Ends

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
	and makes a new list of only the first and last elements of the given list. 

For practice, write this code inside a function.
"""
def return_list_ends(numberList):
	return numberList[:1] + numberList[-1:] if len(numberList) > 1 else numberList

numberList = [int(x) for x in input("Please input list separated with a space: ").split()]
print(*return_list_ends(numberList))

input()