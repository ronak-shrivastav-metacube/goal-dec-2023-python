# Define the custom exception class
class InvalidPasswordException(Exception):
    pass

# User input for password
password = input("Enter a password: ")

try:
    # Check the length of the password
    if len(password) < 8:
        raise InvalidPasswordException
    else:
        # If the password is valid, display a success message
        print("Password is valid.")
except InvalidPasswordException:
    # Handle the exception and display a user-friendly message
    print("Invalid password! Password length should be at least 8 characters long.")
