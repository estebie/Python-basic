def check_prime(number):
	divisors = [x for x in range(2, number-1) if number % x == 0]
	if not divisors:
		print(number, "Is a prime number!")
	else:
		print("Can be divided with :", *divisors)

integer = int(input("Please input an integer: "))
check_prime(integer)

input()

