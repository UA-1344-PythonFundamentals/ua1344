import random

class Призрак(object):
    def __init__(self):
        self.цвет = random.choice(["белый", "черный", "синий", "красный"])

призрак = Призрак()
print(призрак.цвет)
