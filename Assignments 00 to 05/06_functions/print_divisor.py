# ---------------------------------------------------
# Program to Find and Print All Divisors of a Number
# This program takes an integer input from the user 
# and prints all of its divisors.
# ---------------------------------------------------

def print_divisors(num: int):
    """ Prints all divisors of the given number """
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Iterate from 1 to num to check for divisors
        if num % i == 0:  # If num is perfectly divisible by i, it's a divisor
            print(i, end=" ")  # Print divisors on the same line

def main():
    """ Gets user input and calls the print_divisors function """
    num = int(input("Enter a number: "))  # Get a number from the user
    print_divisors(num)  # Call function to print divisors

if __name__ == '__main__':
    main()
