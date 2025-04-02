# ---------------------------------------------------
# Program to Double a Number
# This program takes a user-inputted integer, doubles it, 
# and prints the result. It also handles invalid input.
# ---------------------------------------------------

def double(num: int) -> int:
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    """
    Asks the user for a number, calls the double() function, and prints the result.
    """
    try:
        num = int(input("Enter a number: "))
        print(f"Double that is {double(num)}")
    except ValueError:
        print("⚠️ Please enter a valid integer.")

if __name__ == '__main__':
    main()
