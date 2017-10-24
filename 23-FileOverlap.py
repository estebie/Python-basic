""" 
Exercise 23: File Overlap

Given two .txt files that have lists of numbers in them, 
	find the numbers that are overlapping. 

One .txt file has a list of all prime numbers under 1000, 
	and the other .txt file has a list of happy numbers up to 1000.

"""

def file_to_number_list(filename):
	numberList = []

	with open(filename, 'r') as file:
		numberList = [line.strip() for line in file.readlines()]

	return numberList

first_list = file_to_number_list('23-HappyNumbers.txt')
second_list = file_to_number_list('23-PrimeNumbers.txt')
print("The common number in the list are: ")
print(*list(filter(lambda number: number in second_list, first_list)))
input()

