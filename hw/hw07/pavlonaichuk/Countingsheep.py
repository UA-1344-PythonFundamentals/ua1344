def count_sheeps(sheep):
    return sum(1 for s in sheep if s)

sheep_array = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]

print(count_sheeps(sheep_array))
