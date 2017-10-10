def remove_duplicate(numberList):
	return list(set(numberList))


numberList = [1,2,3,4,5,5,1,2,3,5,6,8,90,199,3,4,5]
print(*remove_duplicate(numberList))
input()