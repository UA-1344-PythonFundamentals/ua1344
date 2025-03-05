import  re

def password_verification(password):
    errors = []

    if len(password) < 6 or len(password) > 16:
        errors.append("Password must be between 6 and 16 characters long.")
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        errors.append("The password must contain at least one lowercase and one uppercase letter.")
    if not re.search("[0-9]", password) or not re.search("[$#@]", password):
        errors.append("The password must contain at least one number and one special character ($, # or @)")
    if errors:
        return "\n".join(errors)
    return "The password is correct."
user_password = input("Enter your password: ")

result = password_verification(user_password)

print(result)