"""
Program: Dice Simulator
----------------------
Simulates rolling two dice, three times.
Prints the results of each die roll.
This program is used to demonstrate variable scope.
"""

import random  # Importing the random library to simulate dice rolls

# Defining the number of sides on a die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their values and total.
    """
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    total = die1 + die2  # Calculating total
    
    # Printing the values and total of two dice
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    die1 = 10  # Local variable in main function
    print(f"die1 in main() starts as: {die1}")
    
    # Rolling dice three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    print(f"die1 in main() is: {die1}")  # Checking if die1 in main() is unchanged

# Calling the main function
if __name__ == '__main__':
    main()
