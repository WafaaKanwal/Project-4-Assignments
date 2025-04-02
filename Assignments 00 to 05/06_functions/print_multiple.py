# ---------------------------------------------------
# Program to Print a Message Multiple Times
# This program takes a message and a repeat count from the user
# and prints the message the specified number of times.
# ---------------------------------------------------

def print_multiple(message: str, repeats: int):
    """ Prints the given message the specified number of times """
    for _ in range(repeats):  # Loop to repeat message 'repeats' times
        print(message)  # Print the message each time

def main():
    """ Gets user input and calls the print_multiple function """
    message = input("Please type a message: ")  # Ask for the message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Ask for repeat count
    print_multiple(message, repeats)  # Call function to print message multiple times

if __name__ == '__main__':
    main()
