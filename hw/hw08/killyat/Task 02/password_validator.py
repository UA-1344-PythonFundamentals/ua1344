import re

def is_valid_password(password):
    """
    Checks if the password meets the validation criteria.
    
    Criteria:
    - At least 1 letter between [a-z]
    - At least 1 letter between [A-Z]
    - At least 1 number between [0-9]
    - At least 1 character from [$#@]
    - Minimum length 6 characters
    - Maximum length 16 characters
    """
    if not (6 <= len(password) <= 16):
        return False
    
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    
    return True

# Main program
if __name__ == "__main__":
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password is valid!")
    else:
        print("Password is invalid. Please ensure it meets all criteria:")
        print("- At least 1 lowercase letter (a-z)")
        print("- At least 1 uppercase letter (A-Z)")
        print("- At least 1 number (0-9)")
        print("- At least 1 special character ($#@)")
        print("- Length between 6 and 16 characters")