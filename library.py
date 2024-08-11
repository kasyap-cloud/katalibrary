class Book :
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        
class Library :
    def __init__(self):
        self.books = list()
        self.borrowedBooks = list()
        
    def addBook(self, book):
        self.books.append(book)
        
    def viewAvailableBooks(self):
        return list(self.books)
    
    def borrowBook(self, isbn):
        # have to code about borrowing a book form the avilable list
        return 0