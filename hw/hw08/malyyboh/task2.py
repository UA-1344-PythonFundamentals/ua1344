# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

password = input("Please enter the password: ")


def validation_password(password):
    if not 6 <= len(password) <= 16:
        return "Password must be between 6 and 16 characters."
    if not re.search("[a-z]+", password):
        return "Password must contain at least one letter between a-z."
    if not re.search("[A-Z]+", password):
        return "Password must contain one uppercase letter between A-Z."
    if not re.search("[0-9]+", password):
        return "Password must contain at least one number between 0-9."
    if not re.search("[$#@]+", password):
        return "Password must contain at least one character from $#@."
    if re.search("\s", password):
        return "Password cannot contain spaces"

    return "Password is valid"


print(validation_password(password))
