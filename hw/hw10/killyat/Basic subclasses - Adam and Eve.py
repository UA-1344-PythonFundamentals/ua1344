class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God:
    @staticmethod
    def create():
        return [Man(), Woman()]

# Example usage
if __name__ == "__main__":
    adam, eve = God.create()
    print(isinstance(adam, Man))
    print(isinstance(eve, Woman))
    print(isinstance(adam, Human))
    print(isinstance(eve, Human))