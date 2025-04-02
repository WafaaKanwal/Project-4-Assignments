# Program to subtract 7 from a number using a helper function

# Helper function to subtract 7 from the given number
def subtract_seven(num):
    """
    This function takes a number (num) and subtracts 7 from it.
    It then returns the result.
    """
    num -= 7  # Subtract 7 from num
    return num  # Return the updated value

# Main function to run the program
def main():
    """
    This function initializes a number, calls the subtract_seven helper function
    to subtract 7 from the number, and prints the result.
    """
    num = 10  # Initialize num with the value 10 (Changed from 7 to 10 for variety)
    num = subtract_seven(num)  # Call the subtract_seven function and update num
    print("After subtracting 7, the result is: ", num)  # Output the result (expected: 3)

# This is the required code to execute the main function when the program is run
if __name__ == '__main__':
    main()  # Call the main function to start the program
