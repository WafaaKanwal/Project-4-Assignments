# This program prints the first 20 even numbers.

def main():
    count = 0  # Variable to keep track of how many even numbers we printed
    number = 0  # Starting even number

    while count < 20:  # Loop until 20 even numbers are printed
        print(number, end=" ")  # Print numbers in a single line with space
        number += 2  # Move to the next even number
        count += 1  # Increase count

# This provided line is required to call the main function
if __name__ == "__main__":
    main()
