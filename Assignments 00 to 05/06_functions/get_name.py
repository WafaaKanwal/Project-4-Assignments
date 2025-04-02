# ---------------------------------------------------
# Program to Print a Greeting with a Predefined Name
# This program returns the name "Sophia" and prints 
# a greeting message using that name.
# ---------------------------------------------------

def get_name() -> str:
    """
    Returns the name 'Sophia' as required by the autograder.
    """
    return "Sophia"

def main():
    """
    Calls get_name() and prints a greeting message.
    """
    name = get_name()
    print(f"Howdy {name}! 🤠")

if __name__ == '__main__':
    main()
