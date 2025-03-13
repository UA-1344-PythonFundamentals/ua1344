import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Example usage
if __name__ == "__main__":
    ghost = Ghost()
    print(ghost.color)