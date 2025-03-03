def countCharacters(s):

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(countCharacters("hello"))
print(countCharacters("pavlo"))
