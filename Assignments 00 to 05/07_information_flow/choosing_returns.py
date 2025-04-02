# ---------------------------------------------------
# Program to Check If a Person Is an Adult
# This program checks whether the entered age is 
# greater than or equal to the legal adult age.
# ---------------------------------------------------

ADULT_AGE: int = 18  # Age threshold for being considered an adult

def is_adult(age: int) -> bool:
    """
    Returns True if the given age is greater than or equal to the adult age,
    otherwise returns False.
    """
    if age >= ADULT_AGE:  # Compare the given age with ADULT_AGE
        return True
    return False

def main():
    """
    Prompts the user to input an age and checks if they are an adult.
    """
    age = int(input("How old is this person?: "))  # Get age from user input
    print(is_adult(age))  # Call the function and print the result

if __name__ == "__main__":
    main()
