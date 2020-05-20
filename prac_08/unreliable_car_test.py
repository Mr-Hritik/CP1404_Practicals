from prac_08.unreliable_car import UnreliableCar

def main():
    nice_car = UnreliableCar("Nice", 100, 90)
    bad_car = UnreliableCar("Not reliable", 100, 9)
    for i in range(1, 12):
        print("drive {}km:".format(i))
        print("{:10} drove {:2}km".format(nice_car.name, nice_car.drive(i)))
        print("{:10} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(nice_car)
    print(bad_car)

main()