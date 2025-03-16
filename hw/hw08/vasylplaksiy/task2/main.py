import re

def validation(pswd):
    if (len(pswd) >= 6 and
        len(pswd) <= 16 and
        re.search(r"[a-z]", pswd) and
        re.search(r"[A-Z]", pswd) and
        re.search(r"[0-9]", pswd) and
        re.search(r"[$#@]", pswd)):
        return True
    else:
        return False

if(validation(input("write pswd:"))):
    print("valid password")
else:
    print("invalid password")

