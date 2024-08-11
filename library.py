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
    
    def findBook(self, isbn):
        for book in list(set(self.books) | set(self.borrowedBooks)):
            if book.isbn == isbn:
                return book
        raise ValueError("Book not found.")
    
    def borrowBook(self, isbn):
        book = self.findBook(isbn)
        if book in self.borrowedBooks:
            raise ValueError("Book is already borrowed")
        if book in self.books:
            self.books.remove(book)
            self.borrowedBooks.append(book)
        else:
            raise ValueError("Book is not available")