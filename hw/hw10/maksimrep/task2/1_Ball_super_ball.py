class Мяч(object):
    def __init__(self, тип="обычный"):
        self.тип = тип

мяч1 = Мяч()
мяч2 = Мяч("супер")

print(мяч1.тип)
print(мяч2.тип)
