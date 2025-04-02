# This program checks if the user meets the minimum height requirement to ride a rollercoaster.

MIN_HEIGHT = 50  # Minimum required height

def check_height():
    """Asks the user for their height and checks if they meet the requirement."""
    try:
        height = float(input("Enter your height: "))
        if height >= MIN_HEIGHT:
            print("Great! You can ride the rollercoaster!")
        else:
            print("Sorry, you're not tall enough yet. Maybe next time!")
    except ValueError:
        print("Invalid input. Please enter a numerical height.")

def main():
    check_height()

# Call main function
if __name__ == '__main__':
    main()
