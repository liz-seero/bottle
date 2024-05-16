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
import random

class Person:
    def __init__(self, name, age, credit_score):
        self.name = name
        self.age = age
        self.credit_score = credit_score

class Loan:
    def __init__(self, person, car, amount, duration):
        self.person = person
        self.car = car
        self.amount = amount
        self.duration = duration
        self.loan_id = random.randint(1000, 9999)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class LoanSystem:
    def __init__(self):
        self.loans = []
        self.people_with_credit = []

    def grant_loan(self, person, car, amount, duration):
        if person.credit_score >= 600:  # Grant loan if credit score is above 600
            loan = Loan(person, car, amount, duration)
            self.loans.append(loan)
            print(f"Loan granted for {person.name} for {car.make} {car.model}.")

    def add_person_with_credit(self, person):
        self.people_with_credit.append(person)

    def check_credit_score(self, person):
        if person in self.people_with_credit:
            print(f"{person.name}'s credit score is {person.credit_score}.")
        else:
            print("Person not found in the credit system.")

# Sample usage
if __name__ == "__main__":
    loan_system = LoanSystem()

    person1 = Person("Alice", 30, 700)
    person2 = Person("Bob", 35, 550)

    loan_system.add_person_with_credit(person1)
    loan_system.add_person_with_credit(person2)

    car1 = Car("Toyota", "Corolla", 2019)
    car2 = Car("Honda", "Civic", 2020)

    loan_system.grant_loan(person1, car1, 20000, 5)
    loan_system.grant_loan(person2, car2, 15000, 4)

    loan_system.check_credit_score(person1)
    loan_system.check_credit_score(person2)
import random

class Animal:
    def __init__(self, name, species, age, condition="Healthy"):
        self.name = name
        self.species = species
        self.age = age
        self.condition = condition

    def diagnose_condition(self):
        if random.random() < 0.2:
            self.condition = "Sick"
        else:
            self.condition = "Healthy"

class Owner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class AnimalShelter:
    def __init__(self):
        self.animals = []
        self.owners = []

    def admit_animal(self, animal):
        self.animals.append(animal)

    def adopt_animal(self, animal, owner):
        if animal in self.animals:
            self.animals.remove(animal)
            self.owners.append(owner)
            print(f"{animal.name} has been adopted by {owner.name}.")
        else:
            print("Animal not found in the shelter.")

    def diagnose_animals(self):
        for animal in self.animals:
            animal.diagnose_condition()

# Sample usage
if __name__ == "__main__":
    shelter = AnimalShelter()

    animal1 = Animal("Buddy", "Dog", 3)
    animal2 = Animal("Whiskers", "Cat", 2)
    animal3 = Animal("Fido", "Dog", 5)

    owner1 = Owner("Alice", "123 Main St", "555-1234")
    owner2 = Owner("Bob", "456 Oak St", "555-5678")

    shelter.admit_animal(animal1)
    shelter.admit_animal(animal2)
    shelter.admit_animal(animal3)

    shelter.diagnose_animals()

    shelter.adopt_animal(animal1, owner1)
    shelter.adopt_animal(animal2, owner2)
import os
import time
import random
import keyboard

# Define constants for game elements
GROUND = "_"
BRICK = "#"
COIN = "o"
MARIO = "M"

# Define the game board size
BOARD_WIDTH = 20
BOARD_HEIGHT = 10

class SuperMarioGame:
    def __init__(self):
        self.board = [[GROUND] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.mario_pos = [BOARD_HEIGHT - 1, 0]
        self.coins = []

    def generate_coins(self):
        for _ in range(5):
            x = random.randint(0, BOARD_WIDTH - 1)
            y = random.randint(0, BOARD_HEIGHT - 1)
            self.coins.append((x, y))

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if (x, y) == tuple(self.mario_pos):
                    print(MARIO, end=" ")
                elif (x, y) in self.coins:
                    print(COIN, end=" ")
                else:
                    print(self.board[y][x], end=" ")
            print()
        print("Use arrow keys to move Mario. Press 'q' to quit.")

    def move_mario(self, direction):
        if direction == "left":
            new_x = max(0, self.mario_pos[1] - 1)
            self.mario_pos[1] = new_x
        elif direction == "right":
            new_x = min(BOARD_WIDTH - 1, self.mario_pos[1] + 1)
            self.mario_pos[1] = new_x

    def check_collision(self):
        if tuple(self.mario_pos) in self.coins:
            self.coins.remove(tuple(self.mario_pos))
            print("Coin collected!")
        elif self.mario_pos[0] < BOARD_HEIGHT - 1:
            self.mario_pos[0] += 1

    def play(self):
        self.generate_coins()
        while True:
            self.draw_board()
            if keyboard.is_pressed('q'):
                print("Game over.")
                break
            if keyboard.is_pressed('left'):
                self.move_mario("left")
            if keyboard.is_pressed('right'):
                self.move_mario("right")
            self.check_collision()
            time.sleep(0.1)

# Run the game
if __name__ == "__main__":
    game = SuperMarioGame()
    game.play()
import re

def ad_libs_story():
    story = """
    Once upon a time, in a {adjective} {place}, there lived a {noun}.
    This {noun} had a {adjective} {animal} named {name}.
    Every day, {name} would {verb} in the {place}.
    One day, {name} decided to {action}, which {verb} the {noun} very {adjective}.
    The end.
    """

    # Extract placeholders from the story
    placeholders = re.findall(r'{(.*?)}', story)

    # Ask the user to input words for each placeholder
    filled_story = story
    for placeholder in placeholders:
        filled_word = input(f"Enter a {placeholder}: ")
        filled_story = filled_story.replace(f"{{{placeholder}}}", filled_word, 1)

    return filled_story

def main():
    print("Welcome to Ad Libs!")
    print("Let's create a story together.")
    print()
    ad_libs_result = ad_libs_story()
    print()
    print("Here's your story:")
    print(ad_libs_result)

if __name__ == "__main__":
    main()
  
