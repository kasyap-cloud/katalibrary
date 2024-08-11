import unittest
from library import Library, Book

class testLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        
    def testAddBook(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", year=2024)
        self.library.addBook(book)
        self.assertIn(book, self.library.books)

if __name__ == '__main__':
    unittest.main()