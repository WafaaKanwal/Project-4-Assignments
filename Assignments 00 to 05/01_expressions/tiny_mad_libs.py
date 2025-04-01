# This program generates a random "Mad Libs" style sentence based on user input.

import random

# Random sentence templates 
SENTENCE_TEMPLATES = [
    "Today, I saw a {adjective} {noun} that tried to {verb}!",
    "Once upon a time, a {adjective} {noun} decided to {verb} all day.",
    "It's amazing how a {adjective} {noun} can {verb} so well!",
    "Would you believe that a {adjective} {noun} actually {verb} yesterday?"
]

def main():
    # Get the three inputs from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    
    # Pick a random sentence template
    sentence = random.choice(SENTENCE_TEMPLATES)
    
    # Print the final mad libs sentence
    print(sentence.format(adjective=adjective, noun=noun, verb=verb))

# Required line to call main function
if __name__ == '__main__':
    main()
