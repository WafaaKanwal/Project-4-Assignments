def main():
    curr_value = int(input("Enter a number: "))  # Get user input and convert it to an integer

    while curr_value < 100:  # Continue looping until curr_value reaches 100 or more
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print the value in the same line with space

if __name__ == '__main__':
    main()
