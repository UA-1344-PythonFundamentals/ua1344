# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

while 1:
    login = input("Please enter your login: ")
    if login != "First":
        print("Error :( please try again.")
    else:
        print("Congratulation! You've entered the correct login.")
        break
