import unittest
from library import Library, Book

class testLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        
    def testAddBook(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", year=2024)
        self.library.addBook(book)
        self.assertIn(book, self.library.books)
        
    def testBorrowBook(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", year=2024)
        self.library.addBook(book)
        self.library.borrowBook(book.isbn)
        availableBooks = self.library.viewAvailableBooks()
        self.assertNotIn(book, availableBooks)
        
    def testReturnBook(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", year=2024)
        self.library.addBook(book)
        self.library.borrowBook(book.isbn)
        self.library.returnBook(book.isbn)
        availableBooks = self.library.viewAvailableBooks()
        self.assertIn(book, availableBooks)

if __name__ == '__main__':
    unittest.main()