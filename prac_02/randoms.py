import random
dir(random)

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1,101))

print("The smallest number that we could have seen in line 1 is 5 and largest number could be 19.")
print("The smallest number in line 2 could have seen is 3 and largest could have been 9.")
print("The smallest number in line could have been 2.5 and largest could have been 5.49.. in floating point values.")