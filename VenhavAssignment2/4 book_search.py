#search

class Book:
    def __init__(s, title, author, genre, copies_available):
        s.title = title
        s.author = author
        s.genre = genre
        s.copies_available = copies_available

class Library:
    def __init__(s):
        s.books = []

    def add_book(s, book):
        s.books.append(book)
        
    def disp(s):
        for book in s.books:
            print(book.title, book.author, book.genre)

    def search_books(s, keyword, search_by='title'):
        results = []
        s.count = 0
        for book in s.books:
            if search_by == 'title' and keyword in book.title:
                results.append(book)
                s.count += 1
            elif search_by == 'author' and keyword in book.author:
                results.append(book)
                s.count += 1
            elif search_by == 'genre' and keyword in book.genre:
                results.append(book)
                s.count += 1
        for book in results:
            print(book.title, book.author, book.genre)
        return s.count
    


book1 = Book("Python Programming", "John Doe", "Programming", 5)
book2 = Book("Data Science Essentials", "Jane Smith", "Data Science", 3)
book3 = Book("Classic Literature", "Alice Johnson", "Fiction", 2)


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.disp()

# Search for books by title and genre
ele = [ ["Python", 'title'],["axis", 'title'] ,["Fiction", "genre"]
      ]

count = 0
for i in ele:
    search_results = library.search_books(*i) #method calling
    if search_results  > 0:
        count += 1
print(count)

