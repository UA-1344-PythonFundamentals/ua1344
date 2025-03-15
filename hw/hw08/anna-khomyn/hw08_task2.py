import re

def validate_pass(str):
    ptrn = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$'
    if re.match(ptrn, str):
        return True
    else:
        return False
    
def test():
    test = ["qwE1@", 
            "qwERty125",
            "qwERty$#@",
            "qwERty12$",
            "qwerty12#",
            "qwERty12$qwERty12$", 
            "M3wW7PQqz4eb",
            "a0Bw26zZPQ#a26h",
            "Sh{JqE3`2_xgv-#j",
            "u!G=LjrnSp[b<8cJ$~9B",
            "mNy@Bekes#EdU",
            "VxHJUM8f4GcyAVyvp"
    ]
    for t in test:
        print(validate_pass(t), "\t==>>\t", t)

test()

passw = input("\nEnter the password: ")
if validate_pass(passw):
    print("Password is valid ^_^")
else:
    print("Password is not valid!")