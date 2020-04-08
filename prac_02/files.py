name = input("Enter your name: ")
out_file1 = open('name.txt', 'w')
print(name,file=out_file1)

out_file1 = open('name.txt', 'r')
print("Reading file....")
print("Your name is "+ out_file1.readline())
out_file1.close

out_file2 = open('numbers.txt', 'r')
print("Result 1: "+str(int(out_file2.readline()) + int(out_file2.readline())))

sum = 0
out_file2 = open('numbers.txt', 'r')
for i in out_file2:
    sum = sum+int(i)
print("Result 2: "+str(sum))

out_file2.close



