# List Operations Program
# This program allows the user to enter a list of elements and prints the last element of the list.

def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[-1])  # List ka aakhri element print karega

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # User se list le raha hai
    get_last_element(lst)  # List ka aakhri element print karega

if __name__ == '__main__':
    main()
