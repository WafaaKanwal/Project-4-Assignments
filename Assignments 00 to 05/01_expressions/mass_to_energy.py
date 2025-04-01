"""
Program: Einstein's Mass-Energy Calculator
-----------------------------------------
This program calculates energy using Einstein's famous equation E = m * C^2.
It takes user input for mass and outputs the equivalent energy in joules.
"""

# Defining the speed of light constant (meters per second)
SPEED_OF_LIGHT = 299792458

def calculate_energy(mass):
    """
    Computes energy using Einstein's formula E = m * C^2.
    """
    return mass * (SPEED_OF_LIGHT ** 2)

def main():
    """
    Takes mass input from the user and displays the energy output.
    """
    mass = float(input("Enter mass in kilograms: "))
    energy = calculate_energy(mass)
    
    print("\nCalculating energy using E = m * C^2...")
    print(f"Mass (m) = {mass} kg")
    print(f"Speed of Light (C) = {SPEED_OF_LIGHT} m/s")
    print(f"Energy = {energy} joules\n")

# Calling the main function when the script runs directly
if __name__ == '__main__':
    main()
