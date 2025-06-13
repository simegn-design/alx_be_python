class Book:
    """Represents a book with checkout status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        self._is_checked_out = False

class Library:
    """Manages a collection of books."""
    
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)
