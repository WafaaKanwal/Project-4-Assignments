"""
💪 Positive Affirmation Trainer
------------------------------
Practice typing empowering statements correctly 
to reinforce positive self-beliefs.
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user_input = input(f"\n🌟 Please type the following affirmation exactly as shown:\n👉 \"{AFFIRMATION}\"\n\nYour input: ")
        
        if user_input == AFFIRMATION:
            print("\n✅ Great job! You got it right! Keep believing in yourself. \n")
            break  # Correct input milne par loop se bahar nikalna hai
        
        print("\n❌ Oops! That wasn't quite right. Try again! 💪\n")

if __name__ == '__main__':
    main()
