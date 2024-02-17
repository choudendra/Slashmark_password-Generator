import random
import string

def generate_password(length):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        number_of_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("Provide the password length: "))

        for password_index in range(number_of_passwords):
            password = generate_password(password_length)
            print(f"Password {password_index + 1}: {password}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for the number of passwords and password length.")

if __name__ == "__main__":
    main()
