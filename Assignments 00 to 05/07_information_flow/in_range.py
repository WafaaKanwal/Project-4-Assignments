# Program to check if a number is within a specified range (inclusive).
# The user will be prompted to enter a number and the lower and upper bounds of the range.
# The program will then check if the number lies between the bounds, inclusive.

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    """
    Asks the user for a number and checks if it's within the specified range.
    """
    print("Let's check if a number is within a specific range!")
    
    # Asking the user for input
    n = int(input("Please enter a number (n): "))  # The number to check
    low = int(input("Please enter the lower bound of the range (low): "))  # The low bound
    high = int(input("Please enter the upper bound of the range (high): "))  # The high bound

    # Call the in_range function and print the result
    if in_range(n, low, high):
        print(f"Yes, {n} is between {low} and {high}, inclusive!")
    else:
        print(f"No, {n} is not between {low} and {high}.")

if __name__ == '__main__':
    main()
