# This program simulates a secure login system where passwords are stored as SHA256 hashes.
# It checks if the entered password matches the stored hash for the given email.

from hashlib import sha256

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password matches the stored hash for the email.
    
    email: User's email.
    stored_logins: Dictionary of email-to-hashed-password mappings.
    password_to_check: Password to verify.
    """
    if email not in stored_logins:
        print(f"❌ Error: No account found for {email}")
        return False  # Return False if email is not found

    if stored_logins[email] == hash_password(password_to_check):
        print("✅ Login successful!")
        return True
    
    print("❌ Incorrect password. Please try again.")
    return False

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # 'password'
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # 'Karel'
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # '123!456?789'
    }
    
    print("\n🔐 Welcome to Secure Login System 🔐\n")
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    login(email, stored_logins, password)


if __name__ == '__main__':
    main()
