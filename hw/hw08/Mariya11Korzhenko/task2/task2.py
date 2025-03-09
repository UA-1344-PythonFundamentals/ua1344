import re

while True:
    pattern = input("Enter login: ")
    errors = []

    if(len(re.findall("[a-z]", pattern)) == 0):
        errors.append("At least one lower case letter is needed")
        
    if(len(re.findall("[A-Z]", pattern)) == 0):
        errors.append("At least one upper case letter is needed")

    if(len(re.findall("[0-9]", pattern)) == 0):
        errors.append("At least one figure is needed")

    if(len(re.findall("[$#@]", pattern)) == 0):
        errors.append("At least one special char e.g. $#@ is needed")

    if len(pattern)<6 or len(pattern)>16:
        errors.append("login should be more than 6 and less than 16")

    if errors:
        print("\n".join(errors))

    else:
        print ("Login is passed!")
        break
