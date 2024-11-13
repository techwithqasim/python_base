# Main script to run the program

from library_class_inventory import Library
from library_class_utils import calculate_fine, generate_report
from datetime import datetime

def main():
    library = Library()

    # Add books to inventory
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.display_inventory()

    # Borrow and return books
    library.borrow_book("The Great Gatsby", "Alice", days=3)  # Borrow for 3 days
    library.display_inventory()

    # Check overdue books
    overdue_books = library.get_overdue_books()
    print("Overdue Books:")
    for title, borrowed_book in overdue_books.items():
        print(f"{title}: borrowed by {borrowed_book.user}, due on {borrowed_book.due_date.strftime('%Y-%m-%d')}")

    # Return a book
    library.return_book("The Great Gatsby", "Alice")
    library.display_inventory()

    # Check fine calculation for a sample late return
    days_late = 5
    fine = calculate_fine(days_late)
    print(f"Fine for {days_late} days late: ${fine}")

    # Generate and display report for borrowed books
    report = generate_report(library.borrowed_books)
    print("Borrowed Books Report:")
    for entry in report:
        print(entry)

if __name__ == "__main__":
    main()
