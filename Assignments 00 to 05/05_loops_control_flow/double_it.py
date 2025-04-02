# This program takes a number from the user and keeps doubling it until it reaches or exceeds 100.

def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print in the same line with space
        
    print("\n✅ Stopped because the value reached or exceeded 100.")

if __name__ == '__main__':
    main()
