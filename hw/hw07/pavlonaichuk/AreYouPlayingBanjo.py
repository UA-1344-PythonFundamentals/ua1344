def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"

print(are_you_playing_banjo("Rick")) 
print(are_you_playing_banjo("rachel")) 
print(are_you_playing_banjo("Pavlo")) 
print(are_you_playing_banjo("Dima"))