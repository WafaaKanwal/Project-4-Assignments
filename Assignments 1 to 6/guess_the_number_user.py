import random  # Importing the random module to generate guesses

def computer_guess(x):
    """
    A number guessing game where the computer tries to guess the user's chosen number
    within a given range (1 to x) based on user feedback.
    """
    low = 1  # Lower bound of the guessing range
    high = x  # Upper bound of the guessing range
    feedback = ''  # Variable to store user feedback

    # Game instructions
    print(f"Think of a number between 1 and {x}, and I'll try to guess it!")

    # Loop until the computer guesses the correct number
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)  # Computer makes a random guess within the range
        else:
            guess = low  # Only one number left, so this must be the answer

        # Asking the user for feedback
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        # Adjusting the range based on user feedback
        if feedback == 'h':
            high = guess - 1  # Reduce the upper bound
        elif feedback == 'l':
            low = guess + 1  # Increase the lower bound

    # Computer successfully guessed the number
    print(f"Yay! The computer guessed your number {guess} correctly! 🎉")

# Calling the function with an upper limit of 10
computer_guess(10)
