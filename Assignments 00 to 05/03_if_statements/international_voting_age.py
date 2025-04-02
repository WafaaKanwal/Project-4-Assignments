# This program checks voting eligibility based on the user's age for multiple countries.

# Define the voting ages for each country
VOTING_AGE = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

def main():
    # Get the user's age
    age = int(input("How old are you? "))

    # Loop through the dictionary and check voting eligibility
    for country, voting_age in VOTING_AGE.items():
        if age >= voting_age:
            print(f"You can vote in {country} where the voting age is {voting_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {voting_age}.")
    
# Call the main function when executed
if __name__ == '__main__':
    main()
