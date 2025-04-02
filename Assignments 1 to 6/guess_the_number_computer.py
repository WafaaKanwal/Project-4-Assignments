import random  # Importing the random module to generate a random number

def guess(x):
    """
    A number guessing game where the user has to guess a randomly generated number
    within a given range (1 to x).
    """
    random_number = random.randint(1, x)  # Generating a random number between 1 and x
    guess = None  # Initializing the guess variable
    attempts = 0  # Counter for the number of attempts

    # Displaying game instructions
    print(f'Welcome to the Guess the Number game!')
    print(f'Guess a number between 1 and {x}.\n')

    # Loop until the user guesses the correct number
    while guess != random_number:
        try:
            guess = int(input(f'Enter your guess: '))  # Taking user input
            attempts += 1  # Incrementing the attempt counter

            # Providing hints based on the user's guess
            if guess < random_number:
                print('Too low! Try again.')
            elif guess > random_number:
                print('Too high! Try again.')
        except ValueError:
            print("Oops! That's not a valid number. Please enter an integer.")  # Handling invalid input

    # Congratulating the user on guessing correctly
    print(f'Yay, congrats! You guessed the number {random_number} correctly in {attempts} attempts.')

# Calling the function with an upper limit of 10
guess(10)
