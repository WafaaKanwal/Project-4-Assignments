"""
🔢 Number Guessing Game 
-------------------------
A simple game where the user guesses a secret number between 1 and 99.
The program provides hints (too high/too low) until the correct number is guessed.
"""

import random

def main():
    # Secret number generate karein
    secret_number = random.randint(1, 99)
    
    print("\n🎯 I am thinking of a number between 1 and 99...")
    
    while True:
        try:
            # User input 
            guess = int(input("🔢 Enter your guess: "))
            
            
            if guess < 1 or guess > 99:
                print("❌ Please enter a number between 1 and 99!")
                continue  # Invalid input ke case me loop continue 
            
            if guess < secret_number:
                print("📉 Your guess is too low. Try again!\n")
            elif guess > secret_number:
                print("📈 Your guess is too high. Try again!\n")
            else:
                print(f"🎉 Congrats! The number was: {secret_number} 🎯")
                break  # Correct guess hone par loop exit 
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")  # Agar user number na de to 

if __name__ == '__main__':
    main()
