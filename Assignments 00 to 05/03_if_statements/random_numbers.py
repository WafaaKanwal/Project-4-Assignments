# This program generates and prints 10 random numbers between 1 and 100.

import random

NUM_COUNT = 10  # Number of random numbers to generate
LOWER_LIMIT = 1
UPPER_LIMIT = 100

def generate_random_numbers():
    """Generates and prints 10 random numbers between 1 and 100."""
    random_numbers = [random.randint(LOWER_LIMIT, UPPER_LIMIT) for _ in range(NUM_COUNT)]
    print(" ".join(map(str, random_numbers)))

def main():
    generate_random_numbers()

# Call main function
if __name__ == '__main__':
    main()
