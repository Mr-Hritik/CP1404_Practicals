min_length = 3

def main():
    password = get_password()
    asteriks(password)


def asteriks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password of more than {} characters: ".format(min_length))
    while len(password) < min_length:
        print("Enter longer password")
        password = input("Enter password of more than {} characters: ".format(min_length))
    return password


main()