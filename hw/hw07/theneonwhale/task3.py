def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

print("Enter a word to count the characters.")

word = input("Enter your word: ")

print(count_characters(word))
