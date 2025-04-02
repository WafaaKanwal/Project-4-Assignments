# ---------------------------------------------------
# Average Calculation Program
# This program calculates the average of two numbers 
# and demonstrates averaging multiple values step-by-step.
# ---------------------------------------------------

def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2  # Directly returning the average

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final_avg = average(avg_1, avg_2)

    # Improved output formatting
    print(f"Average of 0 and 10: {avg_1}")
    print(f"Average of 8 and 10: {avg_2}")
    print(f"Final average: {final_avg}")

# Required call to main function
if __name__ == '__main__':
    main()
