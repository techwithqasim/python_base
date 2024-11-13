# Module for managing book inventory

from datetime import datetime

inventory = []

def add_book(title, author, due_date=None):
    """Add a book to the inventory with optional due date."""
    book = {
        'title': title,
        'author': author,
        'due_date': due_date  # Due date as a datetime object if needed
    }
    inventory.append(book)
    print(f"Added book: {title} by {author}")

def remove_book(title):
    """Remove a book from the inventory by title."""
    for book in inventory:
        if book['title'] == title:
            inventory.remove(book)
            print(f"Removed book: {title}")
            return
    print(f"Book '{title}' not found in inventory.")

def display_inventory():
    """Display the inventory of books."""
    if not inventory:
        print("No books in inventory.")
    else:
        print("Current Inventory:")
        for book in inventory:
            due = book['due_date'].strftime("%Y-%m-%d") if book['due_date'] else "No due date"
            print(f" - {book['title']} by {book['author']} (Due: {due})")

