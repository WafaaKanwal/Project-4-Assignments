import random  # Importing the random module to generate random passwords

print("Welcome To Your Password Generator!")  # Greeting message

# Defining the character set for the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890"

# Asking the user for the number of passwords to generate
number = input("Amount of passwords to generate: ")
number = int(number)  # Converting input to integer

# Asking the user for the desired length of each password
length = input("Input your password length: ")
length = int(length)  # Converting input to integer

print("\nHere are your passwords: \n")  # Displaying generated passwords

# Loop to generate multiple passwords
for _ in range(number):
    password = ""  # Initializing an empty string for the password
    for _ in range(length):
        password += random.choice(chars)  # Randomly selecting characters from the charset
    print(password)  # Printing the generated password

print("\nHave a great day!")  # Friendly closing message
