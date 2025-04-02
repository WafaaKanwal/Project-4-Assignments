import time  # Importing the time module to create a delay

def countdown(t):
    """
    Function to run a countdown timer.
    The user inputs a time in seconds, and the countdown runs until it reaches zero.
    """
    while t:  # Loop runs until the timer reaches zero
        mins, secs = divmod(t, 60)  # Convert seconds into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format the timer as MM:SS
        print(timer, end="\r")  # Print the timer on the same line (overwrite previous)
        time.sleep(1)  # Pause for 1 second
        t -= 1  # Decrease time by 1 second

    print('Timer completed!')  # Message displayed when the timer ends

# Asking the user for input in seconds
t = input("Enter the time in seconds: ")

# Calling the countdown function with user input converted to an integer
countdown(int(t))
