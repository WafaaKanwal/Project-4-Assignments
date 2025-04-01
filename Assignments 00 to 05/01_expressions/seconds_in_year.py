"""
Program: Seconds in a Year Calculator
-----------------------------------
This program calculates the total number of seconds in a year
using predefined constants and displays the result.
"""
# Constants for time calculations
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def calculate_seconds_in_year():
    """Calculates the total number of seconds in one year."""
    return DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

def main():
    """Computes and displays the total seconds in a year."""
    total_seconds = calculate_seconds_in_year()
    print(f"There are {total_seconds} seconds in a year!")

# Calling the main function 
if __name__ == '__main__':
    main()
