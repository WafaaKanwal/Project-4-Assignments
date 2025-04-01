# This program calculates the sum of a list of numbers and prints the result.

# Function to calculate the sum of a list of numbers
def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0  # Initialize sum variable
    for number in numbers:
        total_so_far += number  # Add each number to the total
    return total_so_far

# Main function to execute the program
def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # List of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Compute the sum
    print(sum_of_numbers)  # Output the sum

# Ensuring main() runs when script is executed
if __name__ == '__main__':
    main()
