integer = int(input("Please input a number to be divided: "))

print(list(filter(lambda number: (integer % number) == 0, range(1, integer+1))))
input()