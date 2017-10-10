import random

password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
randomValue=random.sample(password,10)

print("The generated password is", "".join(randomValue))
input()