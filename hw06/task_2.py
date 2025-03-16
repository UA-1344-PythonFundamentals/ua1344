# Start an infinite loop to keep asking for the login until it's correct
while True:
    # Ask the user for their login
    login = input("Enter your login: ")
    
    # Check if the login is "First"
    if login == "First":
        print("Welcome, First!")
        break  # Exit the loop once the correct login is entered
    else:
        print("Error: Invalid login. Please try again.")