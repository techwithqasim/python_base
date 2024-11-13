# Utility functions (like fine calculation)

import math
from datetime import datetime

def calculate_fine(days_late):
    """Calculate the fine based on days late."""
    return math.ceil(days_late * 0.5)  # Example formula

def generate_report(borrowed_books):
    """Generate a report for borrowed books."""
    report = [
        f"{title}: borrowed by {borrowed_book.user} (Due: {borrowed_book.due_date.strftime('%Y-%m-%d')})"
        for title, borrowed_book in borrowed_books.items()
    ]
    return report
