import random

first_list = random.sample(range(15), 8)
second_list = random.sample(range(11), 10)

print("The first number list is: ", first_list)
print("The second number list is: ", second_list)
print("The common number in the lists are: ")
print(list(filter(lambda number: number in second_list, first_list)))

input()