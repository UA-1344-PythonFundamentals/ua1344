def chars_in_str(str):
    """The function calculates the number of characters included in given string, not case-sensitive"""

    str = str.lower()
    result = {}.fromkeys(str, 1)
    for c in result: 
        result[c] = str.count(c)
    return result

print(chars_in_str("hello"))
print(chars_in_str("Anna"))