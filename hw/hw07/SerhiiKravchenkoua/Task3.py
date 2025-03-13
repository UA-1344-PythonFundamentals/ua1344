def number_characters(string):
    symbol_count = {}
    for symbol in string:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1
    return symbol_count

print(number_characters('Helloooo'))