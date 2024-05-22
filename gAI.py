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
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies} available copies)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.available_copies > 0:
                book.available_copies -= 1
                print(f"You have borrowed '{book.title}'. Enjoy reading!")
            else:
                print("Sorry, all copies of this book are currently checked out.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.available_copies += 1
            print(f"Thank you for returning '{book.title}'.")
        else:
            print("Book not found in the library.")

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found in the library.")

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies} available copies)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.available_copies > 0:
                book.available_copies -= 1
                print(f"You have borrowed '{book.title}'. Enjoy reading!")
            else:
                print("Sorry, all copies of this book are currently checked out.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.available_copies += 1
            print(f"Thank you for returning '{book.title}'.")
        else:
            print("Book not found in the library.")

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found in the library.")

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies} available copies)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.available_copies > 0:
                book.available_copies -= 1
                print(f"You have borrowed '{book.title}'. Enjoy reading!")
            else:
                print("Sorry, all copies of this book are currently checked out.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.available_copies += 1
            print(f"Thank you for returning '{book.title}'.")
        else:
            print("Book not found in the library.")

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found in the library.")

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
