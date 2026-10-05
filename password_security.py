import random
import string


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


print("========================================")
print("       PASSWORD SECURITY TOOL")
print("========================================")

while True:
    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter your password: ")

        strength = check_strength(password)

        print("\nPassword Strength:", strength)

    elif choice == "2":
        try:
            length = int(input("Enter password length: "))

            if length < 8:
                print("Password length should be at least 8.")
            else:
                password = generate_password(length)

                print("\nGenerated Password:", password)
                print("Strength:", check_strength(password))

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("\nThank you for using Password Security Tool! 🔐")
        break

    else:
        print("Invalid choice!")