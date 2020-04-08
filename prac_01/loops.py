for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 110, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
num=int(input("Enter number of stars: "))
for i in range(num):
    print("*", end=' ')
for i in range(0, num+1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")
