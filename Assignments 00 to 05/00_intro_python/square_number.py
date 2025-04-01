# This program prompts the user to enter a number and calculates its square.

def main():
    # Prompt the user for a number and convert it to a float
    num = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = num ** 2
    
    # Print the result 
    print(f"{num} squared is {square}")

if __name__ == '__main__':
    main()
