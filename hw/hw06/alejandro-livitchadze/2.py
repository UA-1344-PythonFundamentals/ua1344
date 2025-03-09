passphrase = input("Enter your passphrase: ")

while passphrase != "First":
    print("Wrong! Try again.")
    passphrase = input("Enter your passphrase: ")
else:
    print("Correct! You may pass.")