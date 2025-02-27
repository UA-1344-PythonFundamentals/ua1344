def count_chars(text):
    char_count = {}
    for i in text:
        if char_count.get(i):
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

print(count_chars("dsfdsfdsffff"))
