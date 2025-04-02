# ---------------------------------------------------
# Program to Extract and Print the Ones Digit of a Number
# This program takes an integer input from the user
# and extracts its ones digit using the modulo operator (%).
# ---------------------------------------------------

def print_ones_digit(num: int):
    """Extracts and prints the ones digit of the given number."""
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    """Takes user input and calls print_ones_digit to display the result."""
    
    try:
        num = int(input("Enter a number: "))  # Prompt user for input
        print_ones_digit(num)  # Call function to process and print the ones digit
    except ValueError:
        print("Invalid input! Please enter a valid integer.")  # Handle non-integer inputs

if __name__ == '__main__':
    main()
