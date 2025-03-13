def count_characters(text):
    """
    Calculates the number of characters in a given string and returns a list of characters.
    
    Args:
        text (str): The input string to analyze.
    
    Returns:
        list: A list of individual characters in the string.
    
    Example:
        >>> count_characters("hello")
        ['h', 'e', 'l', 'l', 'o']
    """
    return list(text)

input_string = "hello"
result = count_characters(input_string)
print(f"Input: \"{input_string}\"")
print(f"Output: {result}")