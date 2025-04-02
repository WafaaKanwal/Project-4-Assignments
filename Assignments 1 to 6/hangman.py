import random  # Importing the random module to select a random word
import string  # Importing the string module to handle alphabets

def get_word():
    """
    Function to select a word based on user-selected difficulty.
    The user chooses from 'easy', 'medium', or 'hard' difficulty levels.
    """
    words = {
        "easy": ["cat", "dog", "hat"],  # Simple 3-letter words
        "medium": ["table", "chair", "house"],  # Moderate difficulty words
        "hard": ["elephant", "giraffe", "mountain"]  # Longer and tougher words
    }

    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in words:
            return random.choice(words[difficulty])  # Randomly selecting a word from the chosen difficulty level
        else:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")

def hangman():
    """
    A Hangman game where the player guesses letters of a hidden word within a limited number of attempts.
    The player gets 6 lives, and incorrect guesses reduce the life count.
    """
    while True:  # Outer loop to allow the user to play again
        word = get_word()  # Get a random word based on the selected difficulty
        word_letters = set(word)  # Set of unique letters in the word
        alphabet = set(string.ascii_lowercase)  # All lowercase letters
        used_letters = set()  # Stores letters guessed by the user
        lives = 6  # Number of attempts

        # Displaying game instructions
        print("\nWelcome to Hangman!")
        print(f"The word has {len(word)} letters. Good luck!")

        # Main game loop
        while len(word_letters) > 0 and lives > 0:
            print(f"\nYou have {lives} lives left.")
            print("Used letters: ", ", ".join(used_letters))  # Showing guessed letters
            
            # Displaying the current state of the word (guessed letters & blanks)
            word_display = [letter if letter in used_letters else '_' for letter in word]
            print("Word: ", " ".join(word_display))

            # Taking user input for guessing a letter
            user_letter = input("Guess a letter: ").lower()

            # Checking if the guessed letter is valid
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)  # Adding guessed letter to used letters
                
                if user_letter in word_letters:
                    word_letters.remove(user_letter)  # Removing correctly guessed letter from the word set
                    print("Good guess!")
                else:
                    lives -= 1  # Reducing a life for incorrect guess
                    print(f"Wrong guess! '{user_letter}' is not in the word.")
            elif user_letter in used_letters:
                print("You already guessed that letter. Try again.")  # If letter is already guessed
            else:
                print("Invalid input. Please enter a valid letter.")  # If input is not a letter

        # Checking game result
        if lives == 0:
            print(f"\nYou lost! The word was '{word}'.")  # Losing message
        else:
            print(f"\nCongratulations! You guessed the word '{word}'!")  # Winning message

        # Asking the player if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # Exiting the game loop

# Calling the function to start the game
hangman()
