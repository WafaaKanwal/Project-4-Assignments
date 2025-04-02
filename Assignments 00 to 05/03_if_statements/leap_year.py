# This program checks if the entered year is a leap year or not.

def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    # Take user input for the year
    year = int(input("Enter a year: "))

    # Check if it's a leap year using the function
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call the main function when executed
if __name__ == '__main__':
    main()
