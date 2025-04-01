# This program asks for your favorite animal and responds with excitement.

def main():
    # Ask the user for their favorite animal
    animal = input("\nWhat's your favorite animal? ").strip()
    
    # Print a fun response
    print(f"\nWow! My favorite animal is also {animal.capitalize()}!\n")

# Run the main function
if __name__ == '__main__':
    main()
