while True:
    user_login = input("Enter your login: ")
    if user_login != "First":
        print("Error, incorrect login")
    else:
        print(f"You have successfully login under the name: {user_login}")
        break
