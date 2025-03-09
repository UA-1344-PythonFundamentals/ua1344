def calculate_number_characters(string: str):
    characters_dict = {}
    for i in string:
        if i not in characters_dict.keys():
            characters_dict.update({i: string.count(i)})

    return characters_dict


print(calculate_number_characters("Hello"))
