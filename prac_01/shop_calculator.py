items=int(input("Enter the number: "))
total=0
while items<0 :
    print("Invalid number of items.\n Enter number of items again...")
if items==0 :
    print("No items")
else :
    for i in range(1, items+1):
        price = float(input("Enter price of item " + str(i)+": "))
        total = total + price
finalPrice=total-(total*0.1)
print("Total Price for "+str(items)+" items is "+"{:.2f}".format(finalPrice))
