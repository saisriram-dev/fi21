# Composition = It means there is a "has-a" relationship
# A library has a collection of books

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create a library
library = Library("Bloomberry library")

# Create some books
# They can exist independently. Library is just housing them
book1 = Book("Harry Potter and the Philosopher's Stone", "JK Rowling")
book2 = Book("Harry Potter and the Chamber of Secrets", "JK Rowling")
book3 = Book("Harry Potter and the Prisoner of Azkaban", "JK Rowling")
book4 = Book("Harry Potter and the Goblet of Fire", "JK Rowling")   
book5 = Book("Harry Potter and the Order of the Phoenix", "JK Rowling")
book6 = Book("Harry Potter and the Half-Blood Prince", "JK Rowling")
book7 = Book("Harry Potter and the Deathly Hallows", "JK Rowling")

# Add the books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)

# List the books in the library
for book in library.list_books():
    print(book)

# Output:
# Harry Potter and the Philosopher's Stone by JK Rowling
# Harry Potter and the Chamber of Secrets by JK Rowling
# Harry Potter and the Prisoner of Azkaban by JK Rowling
# Harry Potter and the Goblet of Fire by JK Rowling
# Harry Potter and the Order of the Phoenix by JK Rowling
# Harry Potter and the Half-Blood Prince by JK Rowling
# Harry Potter and the Deathly Hallows by JK Rowling
