

def get_integer(prompt):
    while True:
        try:
            integer_input = int(input(prompt))
            return integer_input
        except ValueError:
            print("Ongeldige invoer. Voer een integer in.")

def get_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Ongeldige invoer. Voer een float in.")

def get_string(prompt):
    return input(prompt)

def get_letter(prompt):
    while True:
        letter = input(prompt).strip()
        if len(letter) == 1 and letter.isalpha():
            return letter.upper()
        else:
            print("Ongeldige invoer. Vul 1 letter in.")


