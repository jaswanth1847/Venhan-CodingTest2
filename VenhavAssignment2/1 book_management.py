#Book Management

class Book:
    def __init__(s, title, author, isbn, genre, quantity):
        s.title = title
        s.author = author
        s.isbn = isbn
        s.genre = genre
        s.quantity = quantity

class Library:
    def __init__(s):
        s.books = []

    def add_book(s, book):
        s.books.append(book)

    def remove_book(s, book):
        if book in s.books:
            s.books.remove(book)
        else:
            print("Book not found in the library.")

    def update_book_info(s, book, new_title, new_author, new_quantity):
        if book in s.books:
            book.title = new_title
            book.author = new_author
            book.quantity = new_quantity
        else:
            print("Book not found in the library.")

    def display_books(s):
        for book in s.books:
            print(book.title, book.author,book.isbn,book.genre,book.quantity)
    


library = Library()

book1 = Book("Python Programming", "John Doe", "123456789", "Programming", 5)
book2 = Book("Data Science Essentials", "Jane Smith", "987654321", "Data Science", 3)

library.add_book(book1)
library.add_book(book2)

library.display_books()

library.update_book_info(book1, "Python 101", "John Doe Jr.", 10)

library.remove_book(book2)

library.display_books()
