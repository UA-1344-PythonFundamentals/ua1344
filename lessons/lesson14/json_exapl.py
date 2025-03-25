import json

# with open("lessons\\lesson14\\user.json") as file:
#     data = file.read()
#     print(type(data), data)
#     data = json.loads(data)
#     print(type(data), data)

#     # data = json.load(file)
#     # print(type(data), data)
#     # print(data["firstName"])
# print("end")


data = {
    "name": "Liubov",
    "age": 35,
    "city": "Lviv",
    "children": [{"name": "Maksym", "age": 6}],
}


# print(json.dumps(data))

with open("lessons\\lesson14\\data.json", "w") as file:
    json.dump( data, file)
