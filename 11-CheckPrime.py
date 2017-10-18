"""
Exercise 11: Check Prime Number

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
def check_prime(number):
	divisors = [x for x in range(2, number-1) if number % x == 0]
	if not divisors:
		print(number, "Is a prime number!")
	else:
		print("Can be divided with :", *divisors)

integer = int(input("Please input an integer: "))
check_prime(integer)

input()

