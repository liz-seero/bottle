class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library.")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("Book not found.")

    def search_book_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("Book not found.")

# Sample usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532743")
    book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780261102217")

    library.add_book(book1)
    library.add_book(book2)

    library.search_book_by_title("harry potter")
    library.search_book_by_author("J.R.R. Tolkien")

    library.remove_book(book1)

    library.search_book_by_title("harry potter")
