# ---------------------------------------------------
# Program to Identify Odd and Even Numbers in a Range
# This program checks numbers from 10 to 19 and 
# prints whether each is odd or even.
# ---------------------------------------------------

def is_odd(value: int):
    """ Returns True if the given number is odd, otherwise False """
    return value % 2 == 1

def main():
    """ Iterates through numbers 10 to 19 and prints if they are odd or even """
    for num in range(10, 20):
        print(num, "odd" if is_odd(num) else "even", end=" ")

if __name__ == '__main__':
    main()
