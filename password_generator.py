import random
import string

def generate_password(length, include_numbers=True, include_symbols=True):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters

    if include_numbers:
        characters += numbers
    if include_symbols:
        characters += symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("\n===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (min 4): "))
        break
    except:
        print("Enter a valid number.")

num_choice = input("Include numbers? (y/n): ").lower() == "y"
symbol_choice = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, num_choice, symbol_choice)

print("\nGenerated Password:")
print(password)

# Save password
save = input("\nSave password to file? (y/n): ").lower()
if save == "y":
    with open("generated_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to generated_passwords.txt")

print("\nDone!")
