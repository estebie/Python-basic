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