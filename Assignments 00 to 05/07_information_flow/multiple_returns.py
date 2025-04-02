# Function to collect user data and return it as a tuple
def get_user_info():
    """
    Asks the user for their first name, last name, and email address
    and returns all of them in a tuple.
    """
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")

    # Returning the collected data as a tuple
    return first_name, last_name, email_address

# Main function to execute the program and display the result
def main():
    # Get the user information by calling the function
    user_data = get_user_info()

    # Output the received data
    print("Received the following user data:", user_data)

# Required to execute the main function
if __name__ == "__main__":
    main()
