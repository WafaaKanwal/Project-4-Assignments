# List Input Program
# This program prompts the user to input values to form a list and displays the final list when done.

def main():
    values = []  # List to store input values

    while True:
        user_input = input("Enter a value (or press enter to finish): ")  # More descriptive message
        if user_input.strip() == "":  # Checking empty input after stripping spaces
            break  # Exit loop if input is empty
        values.append(user_input)  # Add input to list

    print("Your final list:", values)  # Modified output message


if __name__ == '__main__':
    main()
