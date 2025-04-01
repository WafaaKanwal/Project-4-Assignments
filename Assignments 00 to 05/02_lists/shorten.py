# List Shortening Program
# This program takes a user-input list, removes elements from the end if its length exceeds the MAX_LENGTH,
# and prints the removed items. 

MAX_LENGTH = 3  # Maximum allowed length of the list

def shorten(lst):
    """
    Removes elements from the end of the list until its length becomes MAX_LENGTH.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove last item
        print("Removed:", removed_item)  # Print removed item

def get_list():
    """
    Prompts the user to enter elements one by one and returns the final list.
    """
    user_list = []  
    while True:
        item = input("Enter an element (or press enter to stop): ").strip()
        if item == "":  # Stop when input is empty
            break
        user_list.append(item)
    return user_list

def main():
    user_list = get_list()  # Get list from user
    shorten(user_list)  # Modify list if needed

if __name__ == '__main__':
    main()
