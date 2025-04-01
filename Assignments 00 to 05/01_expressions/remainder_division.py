"""
Program: Remainder Division Calculator
-----------------------------------
This program asks the user for two integers,
performs integer division, and displays the quotient and remainder.
"""

def perform_division(dividend, divisor):
    """
    Computes the quotient and remainder of division.
    """
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulo operation to get remainder
    return quotient, remainder

def main():
    """
    Takes user input for two integers and prints the division result.
    """
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    quotient, remainder = perform_division(dividend, divisor)
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Calling the main function when the script runs directly
if __name__ == '__main__':
    main()
