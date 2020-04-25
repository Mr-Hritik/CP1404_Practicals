COLOUR_TO_CODE = {'AliceBlue' : '#f0f8ff', 'Black' : '#000000', 'cyan1' : '#00ffff', 'BlancedAlmond' : '#ffebcd',
                  'beige' : '#f5f5dc', 'AntiqueWhite' : '#faebd7', 'DarkGreen' : '#006400', 'chocolate' : '#d291e'}

def print_colour():
    max_key_length = max([lem(key) for key in COLOUR_TO_CODE.keys()])
    for colour, code in COLOUR_TO_CODE.items():
        print("{:{col_width}} - {}".format(colour, code, col_width=max_key_length))

def main():
    colour_to_code = {colour.lower() : code for colour, code in COLOUR_TO_CODE.items()}
    colour_name = input("Enter a colour: ").strip().lower()
    while(colour_name!=""):
        print("Colour code is {} for {}".format(colour_to_code.get(colour_name), colour_name))
        colour_name = input("Enter a colour: ").strip().lower()

if __name__ == '__main__':
    main()