import re

def checkPasswordValidity(password):
    if (6 <= len(password) <= 16 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)):
        return "Valid Password"
    else:
        return "Invalid Password"

# Example usage:
if __name__ == "__main__":
    password = input("Enter your password: ")
    print(checkPasswordValidity(password))
