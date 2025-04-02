# ---------------------------------------------------
# Chaotic Counting Program
# This program counts from 1 to 10 but has a random 
# chance of stopping early based on probability.
# ---------------------------------------------------

import random

# Probability of stopping early
DONE_LIKELIHOOD = 0.3  

def chaotic_counting():
    """
    Counts from 1 to 10 but stops randomly based on DONE_LIKELIHOOD.
    """
    for i in range(1, 11):  # Using direct range for clarity
        if done():
            return  # Stops execution if done() returns True
        print(i)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("🚀 I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("✅ I'm done.")

if __name__ == "__main__":
    main()
