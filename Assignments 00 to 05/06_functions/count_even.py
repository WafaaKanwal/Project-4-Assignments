# ---------------------------------------------------
# Program to Count Even Numbers in a List
# This program takes a list of integers from the user 
# and counts how many of them are even.
# ---------------------------------------------------

def count_even(lst):
    """
    Counts and prints the number of even numbers in a given list.
    """
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Total even numbers: {even_count}")

def get_list_of_ints():
    """
    Prompts the user to enter integers until they press enter.
    Returns the list of entered numbers.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ").strip()
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("⚠️ Please enter a valid integer.")

    return lst

def main():
    numbers = get_list_of_ints()
    count_even(numbers)

if __name__ == '__main__':
    main()

