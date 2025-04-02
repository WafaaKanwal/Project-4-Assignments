# This program allows the user to create and interact with a phonebook, 
# where they can add names and phone numbers, view entries, and look up phone numbers.

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    print("\n📞 Welcome to the Phonebook Program!")
    print("Enter names and their phone numbers. Press Enter without typing a name to stop.\n")

    while True:
        name = input("Enter Name: ")
        if name == "":  # Blank input means stop
            break
        number = input(f"Enter Phone Number for {name}: ")
        phonebook[name] = number  # Store in dictionary

    print("\n✅ Phonebook data saved successfully!")
    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    if not phonebook:
        print("\n📂 Your phonebook is empty!")
        return

    print("\n📜 Phonebook Entries:")
    for name, number in phonebook.items():
        print(f"📌 {name} -> {number}")  # Print name and number


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook.
    """
    print("\n🔍 Lookup Mode: Enter a name to find their number. Press Enter to exit.")

    while True:
        name = input("\nEnter Name to Lookup: ")
        if name == "":  # Stop lookup if blank input
            print("\n🔴 Exiting lookup mode.\n")
            break
        if name in phonebook:
            print(f"✅ {name}'s number is {phonebook[name]}")
        else:
            print(f"❌ {name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

    print("\n📴 Program ended. Thank you for using the phonebook!")


# Python boilerplate to run the main function
if __name__ == '__main__':
    main()
