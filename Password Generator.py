import random
import string

print("Password Generation")
print("Length should be between 6 and 1024.")

def get_values(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 6 <= user_input <= 1024:
                return user_input
            else:
                print("Length should be between 6 and 1024.")
        except ValueError:
            print("Only Numbers.")

def get_1_0(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input in ["0", "1"]:
                return int(user_input)
            else:
                print("Enter either 1 or 0.")
        except ValueError:
            print("Only Numbers")

length = get_values("Length of Numbers? ")
easy_to_remember = get_1_0("Easy to Remember? (Select 1 For Yes, 0 For No)")
big_letters = get_1_0("Big Letters? (Select 1 For Yes, 0 For No) ")
randomized_symbols = get_1_0("Randomized symbols? (Select 1 For Yes, 0 For No) ")

selections = [("Big Letters", big_letters), ("Numbers", length), ("Randomized Symbols", randomized_symbols)]

if big_letters == 1:
    big_letters = True
else:
    big_letters = False

if randomized_symbols == 1:
    randomized_symbols = True
else:
    randomized_symbols = False

def generate_password(length, use_uppercase, use_digits, use_symbols, easy_to_remember):
    char = string.ascii_lowercase
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    setofnumbers = string.digits
    
    if use_uppercase:
        char += string.ascii_uppercase
    if use_digits:
        char += string.digits
    if use_symbols:
        char += string.punctuation
        
    if easy_to_remember:

        password = "".join(random.choice(consonants + setofnumbers) + random.choice(vowels) for _ in range(length // 2))
        print("Printing easy-to-remember Password (BE WARE: EASY PASSWORDS ARE EASIER TO CRACK!!!)")
    else:
        password = "".join(random.choice(char) for _ in range(length))
    return password

generated_password = generate_password(length, use_uppercase=bool(big_letters), use_digits=True, use_symbols=bool(randomized_symbols), easy_to_remember=bool(easy_to_remember))

print("\n" f"Generated Password: {generated_password}\n")

if length < 8:
    print("Password less than 8 Characters. Small Characters with numbers can be cracked in around 0.15-25 hours.")
elif 8 <= length < 12:
    print("Password between 8 and 12 characters. Small Characters with numbers can be cracked in around 0.25-5 million years.")
else:
    print("Use Big Characters and Symbols for maximum security!\n")
