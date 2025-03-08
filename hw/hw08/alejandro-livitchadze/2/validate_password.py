import re

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
    return bool(re.match(pattern, password))

password = input("Enter your password: ")

if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")