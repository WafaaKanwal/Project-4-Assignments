# Mad Libs Game - This script generates a fun sentence based on user input.

# Asking the user for words to fill in the blanks
adj = input("Adjective: ")  # Taking an adjective from the user
verb1 = input("Verb: ")  # Taking the first verb from the user
verb2 = input("Verb: ")  # Taking the second verb from the user
famous_person = input("Famous person: ")  # Taking the name of a famous person from the user

# Generating and displaying the Mad Libs story
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)  # Printing the final mad lib sentence
