number = int(input("Please input an integer: "))
check = int(input("Please input a number to check: "))

if number % 2 == 0:
	print("Number is even")
else:
	print("Number is odd")

if number % 4 == 0:
	print ("Number is also a multiple of 4")

if number % check == 0:
	print (number, " can be evenly divided with ", check)

input()