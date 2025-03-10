import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "black", "blue", "red"])
        
ghost = Ghost()
print(ghost.color) 