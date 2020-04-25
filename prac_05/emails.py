def name_from_email(email):
    prefix = email.split('@')[0]
    email_parts = prefix.split('.')
    name = " ".join(email_parts).title()
    return name

def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = name_from_email(email)
        confirm = input("Is your name {}? (Y/N) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")
    for email, name in email_and_name.items():
        print("{} ({})".format(name,email))

main()