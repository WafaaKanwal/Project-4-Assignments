# This program defines and prints the ages of five people based on given conditions.

def main():
    # Define ages based on given conditions
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # Print ages with proper formatting
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")


if __name__ == '__main__':
    main()
