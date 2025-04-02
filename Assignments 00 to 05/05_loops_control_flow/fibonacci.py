# This program generates and prints Fibonacci numbers until the value exceeds 10,000.

MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Saare numbers ek line me print honge
        
        # Fibonacci logic
        curr_term, next_term = next_term, curr_term + next_term  # Swap technique se clean logic

    print()  # New line ke liye

if __name__ == '__main__':
    main()
