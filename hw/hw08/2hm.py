import re


def password_ver(passw):
    errors = []

    if len(passw) < 6 or len(passw) > 16:
        errors.append("Password must contain between 6 and 16 characters.")

    if not re.findall("[a-z]", passw) or not re.findall("[A-Z]", passw):
        errors.append("Password must contain both lowercase and uppercase letters.")

    if not re.findall("[0-9]", passw):
        errors.append("Password must contain at least one number (0-9).")

    if not re.findall("[$@#]", passw):
        errors.append("Password must contain at least one of these special characters: $@#.")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid.")


info = input("Enter password: ")
password_ver(info)
