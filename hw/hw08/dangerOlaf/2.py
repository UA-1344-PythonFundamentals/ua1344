# Task2. 
# Write a Python program to check the validity of a password (input from users).
# 
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between 10-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

while 1:
    passwd = input("Please enter pasword: ")
    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$", passwd) == None:
        print("Your password isn't secure, please try again.")
    else:
        print("Your password is fine.")
        break