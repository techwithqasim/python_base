# Module Containing classes for Library, Book, and BorrowedBook

from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BorrowedBook:
    def __init__(self, book, user, due_date):
        self.book = book
        self.user = user
        self.due_date = due_date

    def is_overdue(self):
        """Check if the book is overdue based on the current date."""
        return datetime.now() > self.due_date

class Library:
    def __init__(self):
        self.inventory = []
        self.borrowed_books = {}

    def add_book(self, title, author):
        """Add a book to the inventory."""
        book = Book(title, author)
        self.inventory.append(book)
        print(f"Added book: {title} by {author}")

    def remove_book(self, title):
        """Remove a book from the inventory by title."""
        for book in self.inventory:
            if book.title == title:
                self.inventory.remove(book)
                print(f"Removed book: {title}")
                return
        print(f"Book '{title}' not found in inventory.")

    def display_inventory(self):
        """Display the inventory of books."""
        if not self.inventory:
            print("No books in inventory.")
        else:
            print("Current Inventory:")
            for book in self.inventory:
                print(f" - {book.title} by {book.author}")

    def borrow_book(self, title, user, days=7):
        """Borrow a book if available, setting a due date."""
        for book in self.inventory:
            if book.title == title:
                due_date = datetime.now() + timedelta(days=days)
                borrowed_book = BorrowedBook(book, user, due_date)
                self.borrowed_books[title] = borrowed_book
                self.inventory.remove(book)
                print(f"Book '{title}' borrowed by {user}. Due in {days} days.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title, user):
        """Return a borrowed book to the inventory."""
        borrowed_book = self.borrowed_books.get(title)
        if borrowed_book and borrowed_book.user == user:
            self.inventory.append(borrowed_book.book)
            del self.borrowed_books[title]
            print(f"Book '{title}' returned by {user}.")
        else:
            print("Invalid return attempt or wrong user.")

    def is_available(self, title):
        """Check if a book is available in the inventory."""
        return any(book.title == title for book in self.inventory)

    def get_overdue_books(self):
        """Get a list of all overdue books."""
        overdue_books = {title: borrowed_book for title, borrowed_book in self.borrowed_books.items() if borrowed_book.is_overdue()}
        return overdue_books
