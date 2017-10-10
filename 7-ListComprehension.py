import random

number_list = random.sample(range(15), 8)
even_list = [x for x in number_list if (x%2 == 0)]
print(number_list)
print(even_list)

input()