"""
Exercise 20: Binary Search

Write a function that takes an ordered list of numbers 
	(a list where the elements are in order from smallest to largest) and another number. 

The function decides whether or not the given number is inside 
	the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""

def binarySort (number_list, integer_to_search):
	min, max = 0, len(number_list)
	mid = max // 2

	while (min != mid):
		mid = (min + max) // 2

		if integer_to_search == number_list[mid]:
			return mid
		if (integer_to_search > number_list[mid]):
			min = mid + 1
		else: 
			max = mid - 1
			
	return -1



if __name__ == "__main__":
	number_list = [2, 5, 6, 7, 8, 9, 13, 22, 23, 26, 29]
	integer_to_search = 15
	print("Number list is: ", *number_list)
	print("The integer to be searched is:", integer_to_search)

	index = binarySort(number_list, integer_to_search)

	if (index != -1):
		print("The index of the value is: ", index)
	else:
		print("Number not found in list")
	input()