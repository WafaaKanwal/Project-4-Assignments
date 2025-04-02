# This program collects numbers from the user and counts how often each number appears.

def get_user_numbers():
    """Collects numbers from the user until a blank line is entered."""
    user_numbers = []
    print("Enter numbers one by one. Press Enter without typing anything to finish.")
    
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")
        if user_input.strip() == "":  # Stop input when blank line is entered
            break
        user_numbers.append(int(user_input))  # Convert input to integer and store
    return user_numbers

def count_occurrences(numbers):
    """Counts how often each number appears using a dictionary."""
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1  # Use `get` for cleaner logic
    return count_dict

def print_counts(count_dict):
    """Prints the occurrences of each number."""
    for num, count in count_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """Runs the number counting program."""
    user_numbers = get_user_numbers()
    count_dict = count_occurrences(user_numbers)
    print_counts(count_dict)

if __name__ == '__main__':
    main()
