# Sophia owns a fruit store, and this program helps her manage the stock of fruits.
# The program will prompt the user for the name of a fruit and display how many are available in stock.

def main():
    """
    This is the main function. It prompts the user to input a fruit and checks how many are available in stock.
    Based on the availability, it will display the quantity or state that the fruit is not available.
    """
    # Ask the user to provide the name of the fruit they want to inquire about.
    fruit_name = input("Enter a fruit: ")

    # Get the stock count for the entered fruit name.
    stock_quantity = num_in_stock(fruit_name)

    # If the stock count is zero, notify the user that the fruit is not available.
    if stock_quantity == 0:
        print("This fruit is not in stock.")
    else:
        # If the fruit is available, print how many are in stock.
        print("This fruit is in stock! Here is how many:")
        print(stock_quantity)

def num_in_stock(fruit):
    """
    This function takes the name of a fruit and returns the number of that fruit in stock.
    If the fruit is not found, it returns 0.
    """
    # Check if the fruit is 'apple', return 2 if true.
    if fruit.lower() == 'apple':
        return 2
    # Check if the fruit is 'durian', return 4 if true.
    if fruit.lower() == 'durian':
        return 4
    # Check if the fruit is 'pear', return 1000 if true.
    if fruit.lower() == 'pear':
        return 1000
    # Return 0 if the fruit is not in stock.
    return 0

# Run the main function 
if __name__ == '__main__':
    main()
