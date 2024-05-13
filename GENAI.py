class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
            print(f"Book '{self.title}' returned successfully.")
        else:
            print(f"Book '{self.title}' is already available in the library.")

    def __str__(self):
        return f"{self.title} by {self.author} - Available Copies: {self.available_copies}/{self.copies}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")

    def search_books(self, query):
        found_books = [book for book in self.books if query.lower() in book.title.lower()]
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(book)
        else:
            print("No books found matching the query.")

    def view_available_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Books")
        print("5. View Available Books")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter title of book to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter title of book to return: ")
            library.return_book(title)
        elif choice == "4":
            query = input("Enter search query: ")
            library.search_books(query)
        elif choice == "5":
            library.view_available_books()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
