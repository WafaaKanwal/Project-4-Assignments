"""
Program: Feet to Inches Converter
---------------------------------
This program converts a measurement in feet to inches.
It takes user input in feet and calculates the equivalent inches
using the conversion factor (1 foot = 12 inches).
"""

# Conversion factor: 1 foot = 12 inches
INCHES_PER_FOOT = 12

def convert_feet_to_inches(feet):
    """
    Converts feet to inches.
    """
    return feet * INCHES_PER_FOOT

def main():
    """
    Takes user input for feet and prints the equivalent inches.
    """
    feet = float(input("Enter the number of feet: "))
    inches = convert_feet_to_inches(feet)
    
    print(f"{feet} feet is equal to {inches} inches!")

# Calling the main function 
if __name__ == '__main__':
    main()
