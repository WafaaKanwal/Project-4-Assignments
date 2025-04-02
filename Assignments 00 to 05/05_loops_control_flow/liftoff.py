"""
🚀 Rocket Countdown Simulator 
---------------------------
Simulates a rocket launch countdown from 10 to liftoff.
Displays numbers in descending order with a final 'Liftoff!' message.
"""

def main():
    print("\nPreparing for launch... Countdown begins! \n")
    
    for i in range(10, 0, -1):  # Loop from 10 down to 1
        print(i, end=" ", flush=True)  # Prints numbers on the same line
    
    print("Liftoff! \n")  # Final message after countdown

if __name__ == '__main__':
    main()
