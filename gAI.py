import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=False):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_lowercase = input("Include lowercase characters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    if password:
        print("Your randomly generated password is:", password)

if __name__ == "__main__":
    main()
