# Module for borrowing and returning books
class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory  # Link to Inventory instance
        self.borrowed_books = {}

    def borrow_book(self, book, user):
        """Borrow a book if available in inventory."""
        if book in self.inventory.books:
            self.borrowed_books[book] = user
            self.inventory.remove_book(book)
            print(f"Book '{book}' borrowed by {user}.")
        else:
            print(f"Book '{book}' is not available.")

    def return_book(self, book, user):
        """Return a book to the inventory."""
        if self.borrowed_books.get(book) == user:
            del self.borrowed_books[book]
            self.inventory.add_book(book)
            print(f"Book '{book}' returned by {user}.")
        else:
            print("Invalid return attempt or wrong user.")

    def is_available(self, book):
        """Check if a book is available in the inventory."""
        return book in self.inventory.books