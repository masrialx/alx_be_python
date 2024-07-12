class Book:
    """A class representing a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library with a collection of books."""
    
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return True
                else:
                    print(f"Sorry, {title} is already checked out.")
                    return False
        print(f"Sorry, {title} not found in the library.")
        return False

    def return_book(self, title):
        """Returns a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                    return True
                else:
                    print(f"Sorry, {title} was not checked out.")
                    return False
        print(f"Sorry, {title} not found in the library.")
        return False

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")

