#Write a function that calculates the number of characters included in given string
#• input: "hello"
#• output: {"h":1, "e": 1, "I":2,"0":1}

def count_str(str_to_calc):
    res = {}
    for i in set(str_to_calc):
        res[i] = str_to_calc.count(i)
    print(res)

count_str("hello")
count_str("Python is awesome")