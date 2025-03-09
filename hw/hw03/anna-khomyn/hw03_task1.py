#   1
str = "Flat is better than nested."

print(f"The word \"better\" appears {str.count("better")} times in the given line")
print(f"The word \"never\" appears {str.count("never")} times in the given line")
print(f"The word \"is\" appears {str.count("is")} times in the given line")

print(str.upper())
print(str.replace('i', '&'))