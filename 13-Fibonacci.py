"""
Exercise 13: Fibonacci

Write a program that asks the user how many 
	Fibonnaci numbers to generate and then generates them. 

Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number 
	in the sequence is the sum of the previous two numbers in the sequence. 
	The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def generate_fibonacci(fiboLength):
	list = []
	a,b = 0, 1
	for x in range(0, fiboLength):
		a, b = a+b, a
		list.append(a)
	return list


fiboLength = int(input("Please input fibonacci sequence length: "))
print(*generate_fibonacci(fiboLength))
input()