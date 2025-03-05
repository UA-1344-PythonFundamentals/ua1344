import re

def create_user():
    pass

def is_valid_password(password):
    
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


password = input("enter your pass: ")


if is_valid_password(password):
    print("ok")
else:
    print("!ok")


__all__ = ["create_user","is_valid_password"]