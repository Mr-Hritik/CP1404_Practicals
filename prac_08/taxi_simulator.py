from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            taxis_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == "D":
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            cost_of_trip = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost_of_trip))
            total_bill += cost_of_trip
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        choice = input(">>> ").upper()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    taxis_list(taxis)

def taxis_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

main()