class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        # creating two lists namely "books" and "borrowedBooks".
        self.books = list()
        self.borrowedBooks = list()

    def addBook(self, book):
        # this line will simply append the book details to the list named "books".
        self.books.append(book)

    def viewAvailableBooks(self):
        # this line will return the available books in the "books" list.
        return list(self.books)

    def findBook(self, isbn):
        # finds the book in combined data of "books" and "borrowedBooks"
        for book in list(set(self.books) | set(self.borrowedBooks)):
            if book.isbn == isbn:
                return book
        raise ValueError("Book not found.")

    def borrowBook(self, isbn):
        # finds a book and checks if it is alredy borrowed, if yes, then throw en error, else change the books location from "books" to "borrowedBooks".
        book = self.findBook(isbn)
        if book in self.borrowedBooks:
            raise ValueError("Book is already borrowed")
        if book in self.books:
            self.books.remove(book)
            self.borrowedBooks.append(book)
        else:
            raise ValueError("Book is not available")

    def returnBook(self, isbn):
        # checks if the book was actually borroweed, if yes then change the location from "borrowedBooks" to "books", else raise an error.
        book = self.findBook(isbn)
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
            self.books.append(book)
        else:
            raise ValueError("Book was not borrowed.")
