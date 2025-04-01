# This program converts temperature from Fahrenheit to Celsius.

def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: ").strip())
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Display the result with improved formatting
    print(f"\nTemperature: {fahrenheit:.1f}°F = {celsius:.2f}°C")

# Calling the main() function.
if __name__ == '__main__':
    main()
