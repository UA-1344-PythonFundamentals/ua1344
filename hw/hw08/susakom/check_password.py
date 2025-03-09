# Check password
# HW08 task 02 Susak Oleksandr
import re
def check_password_validation(password):    
    regex = r"^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[$#@]).+$"
    match = re.search(regex, password)
    if match and len(password) >= 6 and len(password) <=15: 
        print("Password is correct")
    else:
        print("Password is not correct")


