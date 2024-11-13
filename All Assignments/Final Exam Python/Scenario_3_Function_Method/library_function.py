# Main script to run the program

from library_function_inventory import add_book, remove_book, display_inventory
from library_function_transactions import borrowed_books, borrow_book, return_book, is_available
from library_function_utils import calculate_fine, filter_overdue_books, generate_report

def main():
    # Add books to inventory
    add_book("The Great Gatsby", "F. Scott Fitzgerald")
    add_book("1984", "George Orwell")
    display_inventory()

    # Borrow and return books
    borrow_book("The Great Gatsby", "Alice", days=3)  # Borrow for 3 days
    display_inventory()

    # Check overdue books
    overdue_books = filter_overdue_books(borrowed_books)
    print("Overdue Books:")
    for title, info in overdue_books.items():
        print(f"{title}: borrowed by {info['user']}, due on {info['due_date']}")

    # Return a book
    return_book("The Great Gatsby", "Alice")
    display_inventory()

    # Check fine calculation for a sample late return
    days_late = 5
    fine = calculate_fine(days_late)
    print(f"Fine for {days_late} days late: ${fine}")

    # Generate and display report for borrowed books
    report = generate_report(borrowed_books)
    print("Borrowed Books Report:")
    for entry in report:
        print(entry)

if __name__ == "__main__":
    main()