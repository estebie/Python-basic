def return_list_ends(numberList):
	return numberList[:1] + numberList[-1:] if len(numberList) > 1 else numberList

numberList = [int(x) for x in input("Please input list separated with a space: ").split()]
print(*return_list_ends(numberList))

input()