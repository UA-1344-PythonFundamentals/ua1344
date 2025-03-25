class Human:
    def __init__(self, _name):
        self._name = _name
        print(f"Welcome  {_name}")

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def get_arb():
        return "Arbitrary message"

h = Human("Kate")
print(f"Kate is {h.get_species()}")