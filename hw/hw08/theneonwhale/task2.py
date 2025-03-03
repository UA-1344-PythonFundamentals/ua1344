import re

def validate_password(password):
    if (len(password) >= 6 and len(password) <= 16 and # Minimum length 6 characters. Maximum length 16 characters.
        re.search(r'[a-z]', password) and              # At least one lowercase letter
        re.search(r'[A-Z]', password) and              # At least one uppercase letter
        re.search(r'[0-9]', password) and              # At least one digit
        re.search(r'[$#@]', password)):                # At least one special character ($, #, @)
        return True
    else:
        return False

def main():
    while True:
        user_password = input("Enter your password: ")

        if validate_password(user_password):
            print("Password is valid.")
            break
        else:
            print("Password is invalid. Please follow the rules for a valid password.")

main()
