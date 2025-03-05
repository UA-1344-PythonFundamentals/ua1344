def check_login():
    login_name = ""
    expected_name = "First"
    while login_name != expected_name:
        login_name  = str(input("Enter login name:"))
    return login_name

print("Hello " + check_login())