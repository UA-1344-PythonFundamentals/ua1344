def character_count(string):
    """
    This function calculates the frequency of each character in a given string and returns it as a dictionary.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    dict: A dictionary with the characters as keys and their counts as values.
    """
    count_dict = {}
    
    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in count_dict:
            count_dict[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            count_dict[char] = 1
    
    return count_dict

# Запит користувача на введення слова
input_string = input("Enter a string: ")

# Викликаємо функцію і виводимо результат
result = character_count(input_string)
print(result)
