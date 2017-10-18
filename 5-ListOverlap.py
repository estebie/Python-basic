"""
Exercise 5: List Overlap

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common 
	between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python 
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

first_list = random.sample(range(15), 8)
second_list = random.sample(range(11), 10)

print("The first number list is: ", first_list)
print("The second number list is: ", second_list)
print("The common number in the lists are: ")
print(list(filter(lambda number: number in second_list, first_list)))

input()