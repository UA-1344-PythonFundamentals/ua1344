def filter_words(st):
    words = st.split() 
    formatted_sentence = " ".join(words).lower() 
    return formatted_sentence.capitalize()

print(filter_words('HELLO CAN YOU HEAR ME'))
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))