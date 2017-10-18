"""
Exercise 6: Palindrome

Ask the user for a string and print out whether this string is a palindrome or not. 
	(A palindrome is a string that reads the same forwards and backwards.)
"""
string = input("Please input a string: ")

if string[::-1] == string:
	print("String is a palindrome")
else:
	print("String is not a palindrome")

input()