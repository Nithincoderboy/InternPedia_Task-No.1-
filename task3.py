#Task3 - PASSWORD GENERATOR
import secrets
import string
import pyperclip  # For copying to clipboard

def generate_password(length, complexity):
    """Generate a random password based on length and complexity."""
    password_characters = ''
    
    if 'uppercase' in complexity:
        password_characters += string.ascii_uppercase
    if 'lowercase' in complexity:
        password_characters += string.ascii_lowercase
    if 'digits' in complexity:
        password_characters += string.digits
    if 'symbols' in complexity:
        password_characters += string.punctuation
    
    if not password_characters:
        raise ValueError("Please select at least one character type for the password.")
    
    password = ''.join(secrets.choice(password_characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter desired complexity (e.g., uppercase, lowercase, digits, symbols), separated by commas: ").lower().split(',')
        
        for _ in range(num_passwords):
            password = generate_password(length, complexity)
            print("Generated Password:", password)
            copy_choice = input("Do you want to copy this password to clipboard? (yes/no): ").lower()
            if copy_choice == 'yes':
                pyperclip.copy(password)
                print("Password copied to clipboard.")
            print()  # Empty line for readability
        
    except ValueError as e:
        print("Error:", e)
        print("Please enter valid input.")

if __name__ == "__main__":
    main()
