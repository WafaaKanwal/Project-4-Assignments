"""
Dice Roll Simulator
--------------------
This program simulates rolling two six-sided dice and displays their individual values as well as their total.
"""
import random  # Importing random module to simulate dice rolls

DICE_SIDES = 6  # Number of sides on each die

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, DICE_SIDES)

def main():
    """Rolls two dice and prints the results along with their sum."""
    die1 = roll_dice()
    die2 = roll_dice()
    total = die1 + die2
    
    print(f"Each die has {DICE_SIDES} sides.")
    print(f"First die roll: {die1}")
    print(f"Second die roll: {die2}")
    print(f"Total of both dice: {total}")

if __name__ == "__main__":
    main()