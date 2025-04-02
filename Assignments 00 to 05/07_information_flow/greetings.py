# ---------------------------------------------------
# Program to Greet the User Based on Their Name
# ---------------------------------------------------

def greet(name: str) -> str:
    """
    Returns a greeting message for the provided name.
    """
    return f"Greetings {name}!"  # Using f-string for cleaner formatting

def main():
    """
    Main function to ask for user's name and greet them.
    """
    name = input("What's your name? ")  # Prompt the user for their name
    print(greet(name))  # Call greet() to display the greeting

# This line is required to ensure the program runs
if __name__ == '__main__':
    main()
