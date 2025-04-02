import random  # Importing the random module to allow the computer to make a random choice

def play():
    """
    A simple Rock-Paper-Scissors game where the user plays against the computer.
    The user selects Rock (r), Paper (p), or Scissors (s), and the computer randomly chooses one.
    The winner is determined based on the standard rules of the game.
    """
    # Dictionary mapping choices to their full names
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    # Asking the user to make a choice
    user = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()

    # Checking if the user input is valid
    if user not in choices:
        print("Invalid choice.")  # Display an error message if input is incorrect
        return  # Exit the function

    # Computer makes a random choice
    computer = random.choice(list(choices.keys()))

    # Displaying user and computer choices
    print(f"You chose {choices[user]}, Computer chose {choices[computer]}.")

    # Determining the winner based on Rock-Paper-Scissors rules
    if user == computer:
        print("It's a tie!")  # If both choices are the same
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print("You won!")  # Winning conditions
    else:
        print("You lost!")  # If none of the winning conditions are met, the computer wins

# Calling the function to start the game
play()
