# Module for borrowing and returning books

from datetime import datetime, timedelta
from library_function_inventory import inventory, remove_book, add_book

borrowed_books = {}

def borrow_book(title, user, days=7):
    """Borrow a book if available, setting a due date."""
    for book in inventory:
        if book['title'] == title:
            borrowed_books[title] = {
                'user': user,
                'due_date': datetime.now() + timedelta(days=days)
            }
            remove_book(title)
            print(f"Book '{title}' borrowed by {user}. Due in {days} days.")
            return
    print(f"Book '{title}' is not available.")

def return_book(title, user):
    """Return a borrowed book to the inventory."""
    if borrowed_books.get(title, {}).get('user') == user:
        due_date = borrowed_books[title]['due_date']
        del borrowed_books[title]
        add_book(title, "Author", None)  # Adjust author and due_date as needed
        print(f"Book '{title}' returned by {user}. Due date was {due_date}.")
    else:
        print("Invalid return attempt or wrong user.")

def is_available(title):
    """Check if a book is available in the inventory."""
    return any(book['title'] == title for book in inventory)

