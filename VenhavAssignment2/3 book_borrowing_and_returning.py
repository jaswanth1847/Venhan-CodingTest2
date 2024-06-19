#Book Borrowing and Returning:

from datetime import datetime, timedelta

class Book:
    def __init__(s, title, author, book_id):
        s.title = title
        s.author = author
        s.book_id = book_id
        s.is_borrowed = False
        s.borrower_id = None
        s.due_date = None

    def borrow_book(s, borrower_id, days_to_return):
        if not s.is_borrowed:
            s.is_borrowed = True
            s.borrower_id = borrower_id
            s.due_date = datetime.now() + timedelta(days=days_to_return)

    def return_book(s):
        s.is_borrowed = False
        s.borrower_id = None
        s.due_date = None
        
class Borrower:
    def __init__(s, name, membership_id):
        s.name = name
        s.membership_id = membership_id

class Library:
    def __init__(s):
        s.books = []
        s.borrowers = []

    def add_book(s, book):
        s.books.append(book)

    def add_borrower(s, borrower):
        s.borrowers.append(borrower)

    def display_borrowers(s):
        for borrower in s.borrowers:
            print(borrower.name, borrower.membership_id)

    def display_borrowed_books(s):
        for book in s.books:
            if book.is_borrowed:
                print(book.title, book.author,book.due_date)
                


library = Library()

book1 = Book("Python Programming", "Guido van Rossum", 1)
book2 = Book("Data Science Handbook", "Jake VanderPlas", 2)

borrower1 = Borrower("Chintu", 101)
borrower2 = Borrower("Pandu", 102)

library.add_book(book1)
library.add_book(book2)

library.add_borrower(borrower1)
library.add_borrower(borrower2)

book1.borrow_book(101, 14)
book2.borrow_book(102, 7)

library.display_borrowers()
library.display_borrowed_books()
