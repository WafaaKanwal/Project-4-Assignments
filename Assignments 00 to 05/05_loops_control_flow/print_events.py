"""
Even Number Sequence (0 to 38)
--------------------------------
Prints the first 20 terms in the sequence of even numbers 
using Python list comprehension: [i*2 for i in range(20)]
"""

def main():
    print(*[i * 2 for i in range(20)])  # List comprehension 

if __name__ == "__main__":
    main()
