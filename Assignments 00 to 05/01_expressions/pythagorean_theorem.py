"""
Program: Pythagorean Theorem Calculator
----------------------------------------
This program calculates the hypotenuse of a right triangle.
It takes user input for the two perpendicular sides (AB and AC)
and computes the hypotenuse (BC) using the Pythagorean theorem:
    BC² = AB² + AC²
"""

import math  # Importing math module to use sqrt function

def calculate_hypotenuse(ab, ac):
    """
    Calculates the hypotenuse using the Pythagorean theorem.
    """
    return math.sqrt(ab**2 + ac**2)

def main():
    """
    Takes user input for two sides and prints the hypotenuse.
    """
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    
    bc = calculate_hypotenuse(ab, ac)
    
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Calling the main function when the script runs directly
if __name__ == '__main__':
    main()