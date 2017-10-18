"""
Exercise 7: List Comprehension

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 

Write one line of Python that takes this list a and makes a new list 
	that has only the even elements of this list in it.
"""
import random

number_list = random.sample(range(15), 8)
even_list = [x for x in number_list if (x%2 == 0)]
print(number_list)
print(even_list)

input()