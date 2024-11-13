# Utility functions (like fine calculation)

import math
from datetime import datetime

def calculate_fine(days_late):
    """Calculate the fine based on days late."""
    return math.ceil(days_late * 0.5)  # Example formula

def filter_overdue_books(borrowed_books):
    """Filter and return overdue books."""
    current_date = datetime.now()
    overdue_books = {
        title: info for title, info in borrowed_books.items() 
        if info['due_date'] < current_date
    }
    return overdue_books

def generate_report(borrowed_books):
    """Generate a report for borrowed books."""
    report = [
        f"{title}: borrowed by {info['user']} (Due: {info['due_date'].strftime('%Y-%m-%d')})"
        for title, info in borrowed_books.items()
    ]
    return report
