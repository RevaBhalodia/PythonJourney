class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to library.')

   
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f'You borrowed "{title}".')
                else:
                    print(f'"{title}" is not available.')
                return
        print("Book not found.")

   
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f'You returned "{title}".')
                else:
                    print(f'"{title}" was not borrowed.')
                return
        print("Book not found.")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(f'- {book.title} by {book.author}')
library = Library()

book1 = Book("Python Basics", "John Doe")
book2 = Book("Data Science 101", "Jane Smith")

library.add_book(book1)
library.add_book(book2)

library.list_available_books()

library.borrow_book("Python Basics")
library.borrow_book("Python Basics")   

library.return_book("Python Basics")
library.return_book("Python Basics")  
