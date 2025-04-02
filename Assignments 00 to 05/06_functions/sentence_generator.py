# ----------------------------------------------
# Sentence Generator Based on Word Type
# This program takes a word and its part of speech (noun, verb, or adjective)
# and generates a meaningful sentence using predefined templates.
# ----------------------------------------------

def make_sentence(word: str, part_of_speech: int):
    """Generates a sentence using the given word based on its part of speech."""
    
    if part_of_speech == 0:
        # If the word is a noun
        print(f"I can't wait to add this {word} to my amazing collection!")
    elif part_of_speech == 1:
        # If the word is a verb
        print(f"The weather is so nice today, it makes me want to {word} right now!")
    elif part_of_speech == 2:
        # If the word is an adjective
        print(f"As I look outside, the sky appears vast and {word}!")
    else:
        # If the user enters an invalid part_of_speech number
        print("Oops! Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    """Takes user input and calls make_sentence to generate a sentence."""
    
    word = input("Enter a noun, verb, or adjective: ")  # Prompt for the word
    print("What type of word is it?")
    
    try:
        part_of_speech = int(input("Enter 0 for noun, 1 for verb, or 2 for adjective: "))  # Ask for the word type
        make_sentence(word, part_of_speech)  # Generate and print the sentence
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")  # Handle invalid input

if __name__ == '__main__':
    main()
