import random

MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_quick_picks = int(input("Enter number of quick picks: "))
    while number_of_quick_picks < 0:
        print("The number should be greater than zero.")
        number_of_quick_picks = int(input("Enter number of quick picks: "))
    for i in range(number_of_quick_picks):
        numbers = []
        for i in range(6):
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while random_number in numbers:
                random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(random_number)
        numbers.sort()
        print(" ".join("{:2}".format(random_number) for random_number in numbers))

main()
