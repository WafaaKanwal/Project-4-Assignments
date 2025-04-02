# This program simulates a fruit shop where the user can buy different fruits,
# and it calculates the total cost based on the quantity entered.

def main():
    # Dictionary of fruit prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    print("\n🍎 Welcome to the Fruit Shop! 🍍")
    print("Enter how many of each fruit you want to buy. Type 0 if you don't want a fruit.\n")

    total_cost = 0  # Initialize total cost

    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
                if amount_bought < 0:
                    print("❌ Please enter a non-negative number!")
                    continue
                total_cost += price * amount_bought
                break  # Valid input, break loop
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    print(f"\n💰 Your total is **${total_cost:.2f}**")
    print("🛒 Thank you for shopping with us! Have a great day! 😊")


# Python boilerplate to run the main function
if __name__ == '__main__':
    main()
