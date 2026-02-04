'''
Manage books in a library.Class Book with attributes: title, author,
Class Library:
add book,remove book,display books,
Use list of objects,Use inheritance (eBook → Book),Override a method to display details.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}")


class eBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB")

class Library:
    def __init__(self):
        self.books = []   

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                book.display_details()   

library = Library()

b1 = Book("Python Basics", "Guido")
b2 = Book("Data Structures", "Mark")
b3 = eBook("AI Fundamentals", "Andrew", 5)

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.display_books()

library.remove_book("Data Structures")

library.display_books()
