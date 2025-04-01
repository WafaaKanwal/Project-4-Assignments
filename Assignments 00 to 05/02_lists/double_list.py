# This program doubles each element in a list of numbers and prints the result.

# Function to double each element in a list
def double_elements(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each element doubled.
    """
    return [num * 2 for num in numbers]  # Using list comprehension to double elements

# Main function to execute the program
def main():
    num_list: list[int] = [1, 2, 3, 4]  # Initial list of numbers
    doubled_list: list[int] = double_elements(num_list)  # Get the doubled list
    print("Doubled Numbers:", doubled_list)  # Output the doubled list

# Ensuring main() runs when script is executed
if __name__ == '__main__':
    main()
