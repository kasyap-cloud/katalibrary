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
        # code to add book into a list
        return 0