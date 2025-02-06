"""Write a program that will display the following questions for user:
      “What is your name?“
       “How old are you?“
       “Where do you live?“
and will read the user's responses and display the corresponding messages:
      “Hello, (answer(name))“.
      “Your age is  (answer(age))“.
      “You live in  (answer(city))“.   """

# HW01
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")
print("Hello, " + name)
print("Your age is " + age)
print("You live in " + city)


