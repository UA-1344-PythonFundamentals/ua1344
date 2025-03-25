# file = open("lessons\lesson14\data.txt")
# file = open("lessons\lesson14\data2.txt", "w")
# file = open("lesson14\data3.txt", "w")
# file = open("C:\data\github\ua1344\lessons\lesson14\data3.txt", "w")

# file = open("lessons\lesson14\data.txt")

# text = file.read()
# print(1, text)
# text = file.read(10)
# print("2", text)

# text = file.read(10)
# print("3", text)

# text = file.readline()
# print("3", text, file.tell())
# text = file.readline()
# print("3", text, file.tell())
# text = file.readlines()
# print("3", text, file.tell())
# file.seek(20)
# text = file.readlines()
# print("33", text, file.tell())


# for line in file:
#     print(line)
# file.close()
from datetime import datetime
with open("lessons\lesson14\data2.txt", "a") as file:
    import time
    while file.tell() < 1000:
        time.sleep(1)
        file.write(f"test {datetime.now()}\n")

print("end")