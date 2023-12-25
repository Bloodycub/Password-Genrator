import random
import string


def Lengthofpassword(prompt): #Lenght of Password Define
    while True:
        try:
            user_input_Lengthof_password = int(input(prompt)) #Input Lenght of password
            if 6 <= user_input_Lengthof_password <= 1024: #Input must be 6-1024 Numbers
                return user_input_Lengthof_password #Returns Password Lenght
            else:
                print("Length should be between 6 and 1024.")
        except ValueError:  #Input was text or symbols and trows error.
            print("Only Numbers.")

def get_yes_or_no_input(prompt): #Selection Easy Password OR Hard
    while True:
        try:
            user_input = input(prompt)
            if user_input in ["1","0"]:
                return int(user_input)
            else:
                print("Invalid input. Please enter either 1 or 0. ")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length, use_uppercase, use_digits, use_symbols, easy_to_remember):
    valid_characters = string.ascii_lowercase
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    setofnumbers = string.digits

    if use_uppercase:
        valid_characters += string.ascii_uppercase
    if use_digits:
        valid_characters += string.digits
    if use_symbols:
        valid_characters += string.punctuation


    if easy_to_remember:
        password = "".join(random.choice(consonants + setofnumbers) + random.choice(vowels) for _ in range(length // 2))
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!Printing easy-to-remember Password (BE WARE: EASY PASSWORDS ARE EASIER TO CRACK!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        password = "".join(random.choice(valid_characters) for _ in range(length))
    return password

def main():
    print("Password Generation")
    print("Length of Password Should Be Between 6 and 1024.")

    length = Lengthofpassword("Length of Password? ")
    easy_to_remember = get_yes_or_no_input("Easy to Remember? (Select 1 For Yes, 0 For No) For Easy Password big letters wont apply. ")
    big_letters = get_yes_or_no_input("Big Letters? (Select 1 For Yes, 0 For No) ")
    randomized_symbols = get_yes_or_no_input("Randomized symbols? (Select 1 For Yes, 0 For No) ")

    selections = [("Big Letters", big_letters), ("Numbers", length), ("Randomized Symbols", randomized_symbols)]

    big_letters = bool(big_letters)
    randomized_symbols = bool(randomized_symbols)

    generated_password = generate_password(length, use_uppercase=big_letters, use_digits=True, use_symbols=randomized_symbols, easy_to_remember=(easy_to_remember))

    print("\n" f"Generated Password: {generated_password}\n")

    if length < 8:
        print("Password less than 8 Characters. Small Characters with numbers can be cracked in around 0.15-25 hours. \n")
    elif 8 <= length < 12:
        print("Password between 8 and 12 characters. Small Characters with numbers can be cracked in around 0.25-5 million years.\n")
    else:
        print("Use Big Characters and Symbols for maximum security!\n")

if __name__ == "__main__":
    main()
