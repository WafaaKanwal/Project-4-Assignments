# Planetary Weight Calculator

# Dictionary containing gravitational constants for each planet
gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Display available planets to the user
print("Available planets: ", ", ".join(gravity_constants.keys()))

# Get user input for Earth weight
earth_weight = float(input("\nEnter your weight on Earth: "))

# Get user input for planet choice
planet = input("Enter a planet: ")

# Check if the planet is in the dictionary
if planet in gravity_constants:
    planet_weight = round(earth_weight * gravity_constants[planet], 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("Invalid planet name. Please enter a correct planet from the list.")
